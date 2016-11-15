from django.test import TestCase
from grace.members_area.forms import RegisterForm


class RegisterFormBodyTest(TestCase):

    def test_register_form_has_fields(self):
        """ Register form must have 6 fields """
        form = RegisterForm()
        expected = ['username',
                    'password',
                    'name',
                    'cpf',
                    'phone',
                    'email']
        self.assertSequenceEqual(expected, list(form.fields))


class ValidateDataTest(TestCase):

    def test_cpf_is_digit(self):
        """ CPF must only accept digits. """
        form = self.make_validated_form(cpf='abc.000.120-00')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_cpf_is_not_valid(self):
        form = self.make_validated_form(cpf='000.000.000-00')
        self.assertListEqual(['cpf'], list(form.errors))

    def test_cpf_is_valid_without_hyphendots(self):
        """ CPF must be valid without hyphen and dots """
        form = self.make_validated_form(cpf='45445238857')
        self.assertListEqual([], list(form.errors))

    def test_cpf_is_valid_with_hyphendots(self):
        """ CPF must be valid with hyphen and dots """
        form = self.make_validated_form(cpf='454.452.388-57')
        self.assertListEqual([], list(form.errors))

    def test_name_capitalized(self):
        """ Name must be capitalized """
        # JOHN pironson -> John Pironson
        form = self.make_validated_form(name='JOHN pironson')
        self.assertEqual('John Pironson', form.cleaned_data['name'])

    def make_validated_form(self, **kwargs):
        valid = dict(username='Django',
                     password='1234',
                     confirmpass='1234',
                     name='John Pironson',
                     cpf='45445238857',
                     phone='16-98198-6747',
                     email='sir.vavo@gmail.com')

        data = dict(valid, **kwargs)
        form = RegisterForm(data)
        form.is_valid()
        return form


