from django.test import TestCase
from grace.members_area.forms import MemberAreaForm
from honeypot.decorators import check_honeypot


class SubscribeTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_get(self):
        """ GET /registre-se/ must return status_code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use members_area/members_area_form.html"""
        self.assertTemplateUsed(self.response, 'members_area/members_area_form.html')

    def test_html(self):
        """Html must contain input tags"""

        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 13)
        self.assertContains(self.response, 'type="text"', 7)
        self.assertContains(self.response, 'type="password"', 3)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, '<button', 2)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """ Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, MemberAreaForm)


    def test_register_form_has_fields(self):
        """ Register form must have 11 fields """
        form = self.response.context['form']
        self.assertSequenceEqual(['login_username',
                                  'password_username',
                                  'username',
                                  'passw',
                                  'confirmpass',
                                  'name',
                                  'cpf',
                                  'phone',
                                  'email'], list(form.fields))
