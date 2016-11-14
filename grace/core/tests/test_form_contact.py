from django.test import TestCase
from grace.core.forms import HomeContactForm


class ContactFormTest(TestCase):

    def setUp(self):
        self.form = HomeContactForm()

    def test_contact_form_as_fields(self):
        """ Contact form must have 3 fields """
        expected = ['ur_email',
                    'ur_name',
                    'ur_message']
        self.assertSequenceEqual(expected, list(self.form.fields))