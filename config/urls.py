from django.contrib import admin
from django.urls import path, include

# restframework
from rest_framework.routers import DefaultRouter

# Integrations
from users.urls import USERS_ROUTER

V1_ROUTER = DefaultRouter()
V1_ROUTER.registry.extend(USERS_ROUTER.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
]
