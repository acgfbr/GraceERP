from django.core import mail
from django.test import TestCase
from grace.members_area.forms import RegisterForm


class RegisterFormGet(TestCase):

    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['register_form']
        self.assertIsInstance(form, RegisterForm)


class RegisterPostValid(TestCase):

    def setUp(self):
        data = dict(username='Hakory',
                    password='1234',
                    confirmpass='1234',
                    name='Flame',
                    cpf='12345678901',
                    phone='16-98198-6747',
                    email='sir.vavo@gmail.com')

        self.response = self.client.post('/success/', data)

    def test_post(self):
        """ Valid POST should redirect to /success/ """
        self.assertEqual(302, self.response.status_code)

    def test_send_register_confirmation_email(self):
        self.assertEqual(1, len(mail.outbox))


class RegisterPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/success/', {})

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


class RegisterSuccessMessage(TestCase):

    def setUp(self):
        data = dict(username='Hakory',
                    password='1234',
                    confirmpass='1234',
                    name='Flame',
                    cpf='12345678901',
                    phone='16-98198-6747',
                    email='sir.vavo@gmail.com')
        self.response = self.client.post('/success/', data, follow=True)

    def test_message(self):
        self.assertContains(self.response, 'Registro realizado com sucesso!')
