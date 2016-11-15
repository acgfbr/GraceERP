from django.test import TestCase
from grace.members_area.forms import LoginForm
from django.shortcuts import resolve_url as r


class LoginFormGet(TestCase):

    def setUp(self):
        self.response = self.client.get(r('members:members_area'))

    def test_has_form(self):
        """ Context must have login form"""
        form = self.response.context['login_form']
        self.assertIsInstance(form, LoginForm)