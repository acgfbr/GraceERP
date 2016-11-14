from django.test import TestCase


class MemberAreaGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/membros/')

    def test_get(self):
        """ GET /membros/ must return status_code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use members_area/members_area_form.html"""
        self.assertTemplateUsed(self.response, 'members_area/members_area_form.html')

    def test_html(self):
        """Html must contain input tags"""
        tags = (('<form', 2),
                ('<input', 12),
                ('type="text"', 7),
                ('type="password"', 2),
                ('type="email"', 1),
                ('<button', 2))

        for text, count in tags:
            self.assertContains(self.response, text, count)

    def test_csrf(self):
        """ Html must contain csrf """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

