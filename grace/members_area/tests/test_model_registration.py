from django.test import TestCase
from _datetime import datetime
from grace.members_area.models import Registration


class RegistrationModelTest(TestCase):
    def setUp(self):
        self.obj = Registration(username='Django',
                       password='1234',
                       name='John Pironson',
                       cpf='45445238857',
                       phone='16-98198-6747',
                       email='sir.vavo@gmail.com')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Registration.objects.exists())

    def test_creat_at(self):
        """ Registration must have an auto created_at attr. """
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('John Pironson', str(self.obj))

    def test_paid_default_to_False(self):
        """" By default paid must be False """
        self.assertEqual(False, self.obj.paid)