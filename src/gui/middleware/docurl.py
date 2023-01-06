"""
Middleware to supply the documentation URL for the menu template
"""
from django.conf import settings

class DocUrlMiddleware:  # pylint: disable=R0903
    """
    Add the documentation url to the request
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.documentation_url = settings.DOCUMENTATION_URL
        request.documentation_alt_url = settings.DOCUMENTATION_ALT_URL
        response = self.get_response(request)
        return response
