"""The views of the `pages` application."""

from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class HomePageView(View):
    """The logic for the functionality of the website's homepage."""
    template_name = 'home.html'

    def get(self, request: HttpRequest):
        """Return the Homepage of the website."""
        return render(request, self.template_name)
