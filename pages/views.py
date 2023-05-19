"""
The views of the `pages` application.

Views:
    HomePageView:
        The logic for the backend functionality of the website's homepage.
"""

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """The logic for the backend functionality of the website's homepage."""
    template_name = 'home.html'

    def get(self, request: HttpRequest):
        """Return the homepage of the website."""
        return render(request, self.template_name)
