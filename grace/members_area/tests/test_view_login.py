from django.test import TestCase
from grace.members_area.forms import LoginForm


class LoginFormGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['login_form']
        self.assertIsInstance(form, LoginForm)