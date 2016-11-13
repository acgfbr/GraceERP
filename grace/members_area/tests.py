from django.core import mail
from django.test import TestCase
from grace.members_area.forms import RegisterForm, LoginForm
from grace.members_area.views import RegisterFormView


class MemberAreaTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_get(self):
        """ GET /membros/ must return status_code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use members_area/members_area_form.html"""
        self.assertTemplateUsed(self.response, 'members_area/members_area_form.html')

    def test_html(self):
        """Html must contain input tags"""

        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 13)
        self.assertContains(self.response, 'type="text"', 7)
        self.assertContains(self.response, 'type="password"', 3)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, '<button', 2)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class LoginFormTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['login_form']
        self.assertIsInstance(form, LoginForm)

    def test_register_form_has_fields(self):
        """ Register form must have 2 fields """
        form = self.response.context['login_form']
        self.assertSequenceEqual(['username',
                                  'password'], list(form.fields))


class RegisterFormTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['register_form']
        self.assertIsInstance(form, RegisterForm)

    def test_register_form_has_fields(self):
        """ Register form must have 7 fields """
        form = self.response.context['register_form']
        self.assertSequenceEqual(['username',
                                  'password',
                                  'confirmpass',
                                  'name',
                                  'cpf',
                                  'phone',
                                  'email'], list(form.fields))


class RegisterPostTest(TestCase):

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

    def test_register_confirmation_enail_subject(self):
        email = mail.outbox[0]
        expect = 'Confirmação de registro'
        self.assertEqual(expect, email.subject)

    def test_register_confirmation_enail_from(self):
        email = mail.outbox[0]
        expect = 'contato@elitedev.com.br'
        self.assertEqual(expect, email.from_email)

    def test_register_confirmation_enail_to(self):
        email = mail.outbox[0]
        expect = ['contato@elitedev.com.br', 'sir.vavo@gmail.com']
        self.assertEqual(expect, email.to)

    def test__register_confirmation_enail_body(self):
        email = mail.outbox[0]
        self.assertIn('Hakory', email.body)
        self.assertIn('1234', email.body)
        self.assertIn('1234', email.body)
        self.assertIn('Flame', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('16-98198-6747', email.body)
        self.assertIn('sir.vavo@gmail.com', email.body)


class RegisterInvalidPost(TestCase):
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


class RegisterSucessMessage(TestCase):

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
