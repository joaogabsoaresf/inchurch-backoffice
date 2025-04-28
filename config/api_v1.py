from ninja import NinjaAPI

from apps.employees.router import router as employees_router

api = NinjaAPI(version="1.0.0", title="backoffice-v1-1.0.0")
api.add_router('/employees/', employees_router)
