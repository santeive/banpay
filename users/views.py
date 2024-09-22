"""
User and ApiUser views
"""

# Models
from .models import User
from .serializers import UserSerializer

# restframework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status

# python
import requests

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
    
    @action(detail=False, methods=['get'], url_path='studio-ghibli')
    def studio_ghibli(self, request):
        user = request.user
        role_to_endpoint = {
            'films': 'films',
            'people': 'people',
            'locations': 'locations',
            'species': 'species',
            'vehicles': 'vehicles',
        }

        if user.role not in role_to_endpoint:
            return Response({"error": "Role not authorized for Studio Ghibli API"}, status=403)

        endpoint = role_to_endpoint[user.role]
        response = requests.get(f'https://ghibliapi.vercel.app/{endpoint}')
        return Response(response.json())

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)