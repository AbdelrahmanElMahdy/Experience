from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.conf import settings
from rest_framework.authtoken.models import Token
from .models import Rate,Experience
from User.models import User

# Create your tests here.

class Experience_testCase(APITestCase):
    

    def test_Experience(self):
        url=reverse('experience:CreateExp')
        user=User.objects.create_user(
            email="murray@gmail.com",
            username="murray",
            password="testpassword",
        )
        token=Token.objects.get(user=user).key
        data={
            "story":"story",
            "foundation":"foundation"
        }
        headers={'HTTP_AUTHORIZATION':f'Token {token}'}
        
        response = self.client.post(url, data, format='json',**headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
