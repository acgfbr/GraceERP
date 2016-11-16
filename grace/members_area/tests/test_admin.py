from unittest.mock import Mock

from django.test import TestCase
from grace.members_area.admin import RegistrationModelAdmin, Registration, admin


class RegistrationModelAdminTest(TestCase):

    def setUp(self):
        Registration.objects.create(username='Django',
                                    password='1234',
                                    name='John Pironson',
                                    cpf='12345678901',
                                    phone='16-98198-6747',
                                    email='john.pironson@zuckibergson.com')

        self.model_admin = RegistrationModelAdmin(Registration, admin.site)

    def test_has_action(self):
        """ Action mark as_paid should be installed. """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """ It should mark all select registrations as paid. """
        self.call_action()
        self.assertEqual(1, Registration.objects.filter(paid=True).count())

    def test_message(self):
        """ It should send a message to the user """
        mock = self.call_action()

        mock.assert_called_once_with(None, '1 registro foi marcado como pago.')

    def call_action(self):
        queryset = Registration.objects.all()

        mock = Mock()
        old_message_user = RegistrationModelAdmin.message_user
        RegistrationModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)

        RegistrationModelAdmin.message_user = old_message_user

        return mock
