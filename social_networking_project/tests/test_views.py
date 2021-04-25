from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from django.conf import settings
import pytest
import datetime
import os
import unittest
import json





from django.urls import reverse



class TestRestAPI(TestCase):
    """Test cases for test rest API's."""

    def setUp(self):
        """Make user login before each test case run."""
        super().setUp()

    def test_signup_api_success(self):
        """Test user logged in successfully or not."""
        data = {
            'username': 'test_user', 'password': "Download1234",
            'password2': "Download1234", 'email': "test@gmail.com",
            'first_name': "Mukesh", 'last_name': "Shrma"}
        base_url = settings.BASE_URL
        url = '/'.join([base_url, 'rest/user/'])
        response = self.client.post(url, data=data)
        self.assertEqual(response.data['username'], data['username'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])

    def test_signup_api_password_validation(self):
        """Test user logged in successfully or not."""
        data = {
            'username': 'test_user', 'password': "Download1234",
            'password2': "Downlod234", 'email': "test@gmail.com",
            'first_name': "Mukesh", 'last_name': "Shrma"}
        base_url = settings.BASE_URL
        url = '/'.join([base_url, 'rest/user/'])
        response = self.client.post(url, data=data)
        self.assertEqual(response.json()['password'][0], "Password fields didn't match.")

    def test_login_api(self):
        user = User.objects.create(username='test_user', email="test@gmail.com",first_name="Mukesh",last_name= "Shrma")
        user.set_password('Download1234')
        user.save()
        url = '/'.join([settings.BASE_URL, 'api/token/'])
        token_response = self.client.post(url, data={'username': user.username, 'password':'Download1234'})
        data = token_response.content
        token_response_dict = json.loads(data.decode("UTF-8"))
        assert token_response_dict.get("access")
        assert token_response_dict.get("refresh")

    