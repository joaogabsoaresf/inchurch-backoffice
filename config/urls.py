from django.contrib import admin
from django.urls import path
from config.api_v1 import api as api_v1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api_v1.urls),
]
