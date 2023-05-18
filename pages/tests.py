"""Tests for the functionality of the pages application"""

from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    """Tests for the homepage of the website"""
    def test_domain_root_is_a_valid_url(self):
        """The website's domain root is a valid application url."""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_domain_root_returns_homepage_of_website(self):
        """The website's domain root returns the homepage of the website."""
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')

