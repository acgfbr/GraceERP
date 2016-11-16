from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class RegisterMailValid(TestCase):

    def setUp(self):
        data = dict(username='Django',
                    password='1234',
                    name='John Pironson',
                    cnpj='78.543.261/0001-45',
                    cpf='45445238857',
                    phone='16-98198-6747',
                    email='john.pironson@zuckibergson.com')
        self.client.post(r('members:register'), data)
        self.email = mail.outbox[0]

    def test_register_confirmation_email_subject(self):
        expect = 'Confirmação de registro'
        self.assertEqual(expect, self.email.subject)

    def test_register_confirmation_email_from(self):
        expect = 'contato@elitedev.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_register_confirmation_email_to(self):
        expect = ['contato@elitedev.com.br', 'john.pironson@zuckibergson.com']
        self.assertEqual(expect, self.email.to)

    def test_register_confirmation_email_body(self):
        contents = ['Django',
                    '1234',
                    'John Pironson',
                    '78.543.261/0001-45',
                    '45445238857',
                    '16-98198-6747',
                    'john.pironson@zuckibergson.com']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

