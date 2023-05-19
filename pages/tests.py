"""
Tests for the functionality of the pages application

TestCases:
    HomePageTest:
        Tests for the functionality of the website's homepage.
"""

from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    """Tests for the homepage of the website."""
    def test_domain_root_is_a_valid_url(self):
        """The website domain's root is a valid application url."""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_domain_root_url_returns_homepage_of_website(self):
        """The website domain's root url returns the homepage of the website."""
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')
