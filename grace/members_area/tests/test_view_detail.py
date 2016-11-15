from django.test import TestCase

from grace.members_area.models import Registration


class RegistrationDetailGet(TestCase):

    def setUp(self):
        self.obj = Registration.objects.create(username='Hakory',
                                               password='1234',
                                               name='Flame',
                                               cpf='12345678901',
                                               phone='16-98198-6747',
                                               email='sir.vavo@gmail.com')
        self.response = self.client.get('/success/{}/'.format(self.obj.pk))

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
        response = self.client.get('/success/0/')
        self.assertEqual(404, response.status_code)
