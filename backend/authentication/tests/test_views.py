from .test_setup import TestSetUp
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
import json

from authentication.models import User


class TestViews(TestSetUp):

    def test_user_cannot_register(self):
        res = self.client.post(self.register_url)

        # import pdb
        # pdb.set_trace()

        self.assertEqual(res.status_code,400)
    
    def test_user_can_register(self):
        res = self.client.post(self.register_url, self.user_data, formart="json")

        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.data['username'], self.user_data['username'])

        self.assertEqual(res.status_code, 201)
    
    def test_user_can_login(self):
        self.client.post(self.register_url, self.user_data, formart="json")


        res = self.client.post(
            self.login_url, self.user_data, formart="json")
       
        self.assertEqual(res.status_code, 200)


        


