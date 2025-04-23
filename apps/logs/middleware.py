import json
import threading
from django.utils.timezone import now
from apps.logs.models import Logs, check_sensitive
from apps.employees.models.employee import Employee

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_data = {
            'method': request.method,
            'path': request.path,
            'request_headers': dict(request.headers),
            'request_body': self.get_request_body(request),
            'start_time': now(),
        }

        response = self.get_response(request)
        if request_data.get('method') is None:
            return response

        self.save_log_async(request, response, request_data)
        return response

    def save_log_async(self, request, response, request_data):
        def _save():
            try:
                google_user_id = request_data['request_headers'].get('Authorization', '')
                employee = Employee.objects.filter(google_user_id=google_user_id).first()

                action = f"{request_data['method']} {request_data['path']}"
                if 'method' in request_data['request_body']:
                    action += f" {request_data['request_body']['method']}"

                logs = Logs(
                    action=action,
                    employee=employee,
                    request_body=request_data['request_body'],
                    request_headers=request_data['request_headers'],
                    response_body=self.get_response_body(response),
                    response_headers=dict(response.items()),
                    status_code=response.status_code,
                    is_senstive=check_sensitive(request_data['request_body'].get('method', '')),
                )

                logs.save()
            except Exception as e:
                print(f"[Middleware Log Error] {e}")
                # Salvar log mínimo mesmo se ocorrer erro
                try:
                    Logs.objects.create(
                        action=f"{request_data['method']} {request_data['path']}",
                        request_body=request_data['request_body'],
                        request_headers=request_data['request_headers'],
                        status_code=getattr(response, 'status_code', 0),
                    )
                except Exception as inner_e:
                    print(f"[Fallback Log Error] {inner_e}")

        threading.Thread(target=_save).start()

    def get_request_body(self, request):
        try:
            if request.content_type == 'application/json':
                body = request.body.decode('utf-8')
                return json.loads(body or '{}')
        except Exception:
            pass
        return {}

    def get_response_body(self, response):
        try:
            if hasattr(response, 'content') and response.get('Content-Type', '').startswith('application/json'):
                return json.loads(response.content.decode('utf-8') or '{}')
        except Exception:
            pass
        return {}
