
# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(
            email="admin@example.com",
            username="admin", 
            password="adminpassword", 
            role="admin", 
            is_staff=True
        )
        self.token = str(RefreshToken.for_user(self.admin_user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
    def test_create_correct_user(self):
        url = reverse('users-list')
        data = {
            "email": "user@example.com",
            "username": "user1",
            "role": "films",
            "password": "password123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(email="user@example.com").role, "films")

    def test_create_incorrect_user(self):
        url = reverse('users-list')
        data = {
            "email": "user@example.com",
            "username": "user1",
            "role": "coordinator",
            "password": "password123"
        }
        response = self.client.post(url, data)
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        url = reverse('users-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())
    
    def test_retrieve_user(self):
        url = reverse('users-detail', args=[self.admin_user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.admin_user.email)

    

