from django.contrib import admin
from django.urls import path, include

# restframework
from rest_framework.routers import DefaultRouter

# Integrations

urlpatterns = [
    path('admin/', admin.site.urls),
]