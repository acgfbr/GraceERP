from django.core import mail
from django.test import TestCase

from grace.core.forms import HomeContactForm


class NewContactPostValid(TestCase):

    def setUp(self):
        data = dict(ur_email='hakory@elitedev.com',
                    ur_name='Hakory',
                    ur_message='Test message for the win')
        self.response = self.client.post('/#contact', data)

    def test_post(self):
        """ Valid POST should redirect to / """
        self.assertEqual(302, self.response.status_code)

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))


class ContactPostInvalid(TestCase):

    def setUp(self):
        self.response = self.client.post('/#contact', {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, HomeContactForm)

    def test_form_has_erros(self):
        """Must show form input errors"""
        form = self.response.context['form']
        self.assertTrue(form.errors)


class ContactSuccessMessage(TestCase):

    def setUp(self):
        data = dict(ur_email='hakory@elitedev.com',
                    ur_name='Hakory',
                    ur_message='Test message for the win')
        self.response = self.client.post('/#contact', data, follow=True)

    def test_message(self):
        self.assertContains(self.response, 'E-mail enviado com sucesso!')