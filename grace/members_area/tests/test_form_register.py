from django.test import TestCase
from grace.members_area.forms import RegisterForm


class RegisterFormTest(TestCase):

    def setUp(self):
        self.form = RegisterForm()

    def test_register_form_has_fields(self):
        """ Register form must have 7 fields """
        expected = ['username',
                    'password',
                    'confirmpass',
                    'name',
                    'cpf',
                    'phone',
                    'email']
        self.assertSequenceEqual(expected, list(self.form.fields))