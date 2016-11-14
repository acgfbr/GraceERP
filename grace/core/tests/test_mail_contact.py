from django.core import mail
from django.test import TestCase


class ContactMailValid(TestCase):

    def setUp(self):
        data = dict(ur_email='hakory@elitedev.com',
                    ur_name='Hakory',
                    ur_message='Test message for the win')
        self.client.post('/#contact', data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = "Requisição de contato Grace ERP"

        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'hakory@elitedev.com'

        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@elitedev.com.br']

        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = ['Hakory',
                    'hakory@elitedev.com',
                    'Test message for the win']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
