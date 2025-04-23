from django.db import models
from apps.employees.models.employee import Employee

class Logs(models.Model):
    action = models.CharField(max_length=255)
    
    request_body = models.JSONField()
    request_headers = models.JSONField()
    response_body = models.JSONField()
    response_headers = models.JSONField()
    
    status_code = models.IntegerField()
    is_senstive = models.BooleanField(default=False)
    
    employee = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_executed_by"
    )
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        indexes = [
            models.Index(fields=['-created_at'], name='logs_created_at_idx'),
        ]
    
def check_sensitive(method):
    sensitive_methods = [
        'set_new_email',
        'update_tertiarygroup',
    ]
    
    return method in sensitive_methods