from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class RegisterMailValid(TestCase):

    def setUp(self):
        data = dict(username='Hakory',
                    password='1234',
                    confirmpass='1234',
                    name='Flame',
                    cpf='12345678901',
                    phone='16-98198-6747',
                    email='sir.vavo@gmail.com')
        self.client.post(r('members:register'), data)
        self.email = mail.outbox[0]

    def test_register_confirmation_enail_subject(self):
        expect = 'Confirmação de registro'
        self.assertEqual(expect, self.email.subject)

    def test_register_confirmation_enail_from(self):
        expect = 'contato@elitedev.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_register_confirmation_enail_to(self):
        expect = ['contato@elitedev.com.br', 'sir.vavo@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test__register_confirmation_email_body(self):
        contents = ['Hakory',
                    '1234',
                    '1234',
                    'Flame',
                    '12345678901',
                    '16-98198-6747',
                    'sir.vavo@gmail.com']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

