
"""
Tests for User app
"""

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
            "password": "admin123-3"
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

    def test_update_user(self):
        url = reverse('users-detail', args=[self.admin_user.id])
        data = {"username": "newusername"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.admin_user.refresh_from_db()
        self.assertEqual(self.admin_user.username, "newusername")
    
    def test_retrieve_movies_by_role(self):
        user = User.objects.create_user(
            email="user1@example.com",
            password="admin123-3",
            username="user1",
            role="films"
        )
        token = str(RefreshToken.for_user(user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        url = reverse('users-studio-ghibli')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(response.data, list))

    def test_sign_in(self):
        url = reverse('token_obtain_pair')
        data = {
            "email": self.admin_user.email,
            "password": "admin123-3"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)