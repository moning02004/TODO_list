from django.test import TestCase, Client

from .models import User


class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='user0', name='user_0')
        user.set_password('password0')
        user.save()

    def test_login(self):
        client = Client()
        response = client.post('/user/login', {'username': 'user0', 'password': 'password0'})
        self.assertEqual(response.status_code, 302)

    def test_signup(self):
        client = Client()
        response = client.post('/user/signup', {'username': 'user11', 'password1': '1q2w3e4r!', 'password2': '1q2w3e4r!', 'name': 'user_11'})
        self.assertEqual(response.status_code, 302)