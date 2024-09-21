"""
User and ApiUser views
"""

# Models
from .models import User
from .serializers import UserSerializer

# restframework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        elif self.action in ['destroy', 'update', 'partial_update']:
            return [IsAdminUser()]
        return super().get_permissions()

