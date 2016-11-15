from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

from grace.core.forms import HomeContactForm


class HomeGet(TestCase):

    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use index.html """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """Html must contain input tags"""

        tags = (('<form', 1),
                ('<input', 4),
                ('<textarea', 1),
                ('type="text"', 2),
                ('type="email"', 1),
                ('type="submit"', 1))

        for text, count in tags:
            self.assertContains(self.response, text, count)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have index form"""
        form = self.response.context['form']
        self.assertIsInstance(form, HomeContactForm)

    def test_contact_form_as_fields(self):

        """ Contact form must have 3 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['ur_email',
                                  'ur_name',
                                  'ur_message'], list(form.fields))

    def test_member_area_link(self):
        expected = 'href="/membros/"'.format(r('members:members_area'))
        self.assertContains(self.response, expected)

