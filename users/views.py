from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return [IsAuthenticated()]
    #     elif self.action == 'destroy' or self.action == 'update':
    #         return [IsAdminUser()]
    #     return super().get_permissions()
