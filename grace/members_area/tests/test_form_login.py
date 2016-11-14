from django.test import TestCase
from grace.members_area.forms import LoginForm


class LoginFormTest(TestCase):

    def setUp(self):
        self.form = LoginForm()

    def test_login_form_has_fields(self):
        """ Register form must have 2 fields """
        expected = ['username',
                    'password']
        self.assertSequenceEqual(expected, list(self.form.fields))
