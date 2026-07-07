from django.test import TestCase
from django.urls import reverse


class AuthRouteTests(TestCase):
    def test_signin_alias_loads_login_page(self):
        response = self.client.get(reverse('signin'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')
