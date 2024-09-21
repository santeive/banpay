"""
Users app url
"""

# Django
from .views import UserViewSet
from django.urls import path, include

# rest framework
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

USERS_ROUTER = SimpleRouter()
USERS_ROUTER.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(USERS_ROUTER.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]