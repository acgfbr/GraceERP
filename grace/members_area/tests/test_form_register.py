from django.test import TestCase
from grace.members_area.forms import RegisterForm


class RegisterFormBodyTest(TestCase):

    def test_register_form_has_fields(self):
        """ Register form must have 6 fields """
        form = RegisterForm()
        expected = ['username',
                    'password',
                    'name',
                    'cnpj',
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

    def test_cnpj_is_digit(self):
        """ CNPJ must only accept digits. """
        form = self.make_validated_form(cnpj='78.DEF.261/0001-AB')
        self.assertListEqual(['cnpj'], list(form.errors))

    def test_cnpj_is_not_valid(self):
        form = self.make_validated_form(cnpj='00.00.000/0000-00')
        self.assertListEqual(['cnpj'], list(form.errors))

    def test_cnpj_is_valid_without_hyphendots(self):
        """ CNPJ must be valid without hyphen and dots """
        form = self.make_validated_form(cnpj='78543261000145')
        self.assertListEqual([], list(form.errors))

    def test_cnpj_is_valid_with_hyphendots(self):
        """ CNPJ must be valid with hyphen and dots """
        form = self.make_validated_form(cnpj='78.543.261/0001-45')
        self.assertListEqual([], list(form.errors))

    def test_name_capitalized(self):
        """ Name must be capitalized """
        # JOHN pironson -> John Pironson
        form = self.make_validated_form(name='JOHN pironson')
        self.assertEqual('John Pironson', form.cleaned_data['name'])

    def test_cnpj_is_optional(self):
        """ CNPJ is optional """
        form = self.make_validated_form(cpnj='')
        self.assertFalse(form.errors)

    def test_cpf_is_optional(self):
        """ CPF is optional """
        form = self.make_validated_form(cpf='')
        self.assertFalse(form.errors)

    def test_must_inform_cnpj_or_cpf(self):
        """CNPJ and CPF are optional, but one must be informed"""
        form = self.make_validated_form(cnpj='', cpf='')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_phone_is_optional(self):
        """ Phone is optional """
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_email_is_optional(self):
        """ Email is optional """
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_must_inform_phone_or_email(self):
        """Phone and Email are optional, but one must be informed"""
        form = self.make_validated_form(phone='', email='')
        self.assertListEqual(['__all__'], list(form.errors))

    def make_validated_form(self, **kwargs):
        valid = dict(username='Django',
                     password='1234',
                     name='John Pironson',
                     cnpj='78.543.261/0001-45',
                     cpf='454.452.388-57',
                     phone='16-98198-6747',
                     email='john.pironson@zuckibergson.com')

        data = dict(valid, **kwargs)
        form = RegisterForm(data)
        form.is_valid()
        return form


