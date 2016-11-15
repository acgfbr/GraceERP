from django.test import TestCase
from django.shortcuts import resolve_url as r

from grace.members_area.models import Registration


class RegistrationSuccessGet(TestCase):

    def setUp(self):
        self.obj = Registration.objects.create(username='Django',
                                               password='1234',
                                               name='John Pironson',
                                               cpf='12345678901',
                                               phone='16-98198-6747',
                                               email='sir.vavo@gmail.com')

        self.response = self.client.get(r('members:success', self.obj.hashId))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'members_area/members_area_success.html')

    def test_context(self):
        registration = self.response.context['registration']
        self.assertIsInstance(registration, Registration)

    def test_html(self):
        contents = (self.obj.username,
                    self.obj.password,
                    self.obj.name,
                    self.obj.cpf,
                    self.obj.phone,
                    self.obj.email)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class RegistrationDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('members:success', '00000000-0000-0000-0000-000000000000'))
        self.assertEqual(404, response.status_code)
