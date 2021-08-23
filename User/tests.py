from django.test import TestCase
from .models import User
# Create your tests here.

class UserTestCases(TestCase):
    def setUp(self):
        User.objects.create_user(
            email="adam@gmail.com",
            username="adam",
            password="testpassword",
        )
     
        User.objects.create_user(
            email="murray@gmail.com",
            username="murray",
            password="testpassword",
        )

    def test_user(self):
        adam=User.objects.get(email="adam@gmail.com")
        murray=User.objects.get(email="murray@gmail.com")

        self.assertEqual(adam.username, 'adam')
        self.assertEqual(murray.username, 'murray')