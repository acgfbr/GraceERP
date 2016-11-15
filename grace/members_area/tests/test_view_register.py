from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

from grace.members_area.forms import RegisterForm
from grace.members_area.models import Registration


class RegisterFormGet(TestCase):

    def setUp(self):
        self.response = self.client.get(r('members:members_area'))

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['register_form']
        self.assertIsInstance(form, RegisterForm)


class RegisterNewPostValid(TestCase):

    def setUp(self):
        data = dict(username='Hakory',
                    password='1234',
                    confirmpass='1234',
                    name='Flame',
                    cpf='12345678901',
                    phone='16-98198-6747',
                    email='sir.vavo@gmail.com')
        self.response = self.client.post(r('members:register'), data)
        self.hashId = Registration.objects.first().hashId


    def test_post(self):
        """ Valid POST should redirect to /success/hashId/ """
        self.assertRedirects(self.response, r('members:success', self.hashId))

    def test_send_register_confirmation_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_save_registration(self):
        self.assertTrue(Registration.objects.exists())


class RegisterNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('members:register'), {})

    def test_post(self):
        """ Invalid POST should not redirect """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'members_area/members_area_form.html')

    def test_has_form(self):
        form = self.response.context['register_form']
        self.assertIsInstance(form, RegisterForm)

    def test_form_has_erros(self):
        form = self.response.context['register_form']
        self.assertTrue(form.errors)

    def test_dont_save_registration(self):
        self.assertFalse(Registration.objects.exists())

