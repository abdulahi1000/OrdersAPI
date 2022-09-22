from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            "email": "test@gmail.com",
            "username": "text",
            "password": '#Ope1234',
            "last_name": "text last",
            "first_name": "text first",
            "phone_number": "09087654567",
        }


        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    pass
