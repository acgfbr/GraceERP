from django.test import TestCase
from _datetime import datetime
from grace.members_area.models import Registration


class RegistrationModelTest(TestCase):
    def setUp(self):
        self.obj = Registration(username='Hakory',
                       password='1234',
                       name='Flame',
                       cpf='12345678901',
                       phone='16-98198-6747',
                       email='sir.vavo@gmail.com')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Registration.objects.exists())

    def test_creat_at(self):
        """ Registration must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)