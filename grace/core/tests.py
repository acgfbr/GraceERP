from django.test import TestCase
from honeypot.decorators import check_honeypot


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

    def test_contact_form_as_fields(self):

        """ Contact form must have 3 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['ur_email',
                                  'ur_name',
                                  'ur_message'], list(form.fields))

class ContactPostTest(TestCase):
    def test_post(self):
        """ Valid POST should redirect to / """