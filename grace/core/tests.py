from django.core import mail
from django.test import TestCase

from grace.core.forms import HomeContactForm


class HomeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """Html must contain input tags"""

        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 4)
        self.assertContains(self.response, '<textarea', 1)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="submit"', 1)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have index form"""
        form = self.response.context['form']
        self.assertIsInstance(form, HomeContactForm)

    def test_contact_form_as_fields(self):

        """ Contact form must have 3 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['ur_email',
                                  'ur_name',
                                  'ur_message'], list(form.fields))

    def test_member_area_link(self):
        self.assertContains(self.response, 'href="/membros/"')


class ContactPostTest(TestCase):

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

    def test_contact_email_subject(self):
        email = mail.outbox[0]
        expect = "Requisição de contato Grace ERP"

        self.assertEqual(expect, email.subject)

    def test_contact_email_from(self):
        email = mail.outbox[0]
        expect = 'hakory@elitedev.com'

        self.assertEqual(expect, email.from_email)

    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['sir.vavo@gmail.com']

        self.assertEqual(expect, email.to)

    def test_contact_email_body(self):
        email = mail.outbox[0]

        self.assertIn('Hakory', email.body)
        self.assertIn('hakory@elitedev.com', email.body)
        self.assertIn('Test message for the win', email.body)


class ContactInvalidPost(TestCase):

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

class ContactSucessMessage(TestCase):
    def test_message(self):
        data = dict(ur_email='hakory@elitedev.com',
                    ur_name='Hakory',
                    ur_message='Test message for the win')