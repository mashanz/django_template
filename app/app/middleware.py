from django.shortcuts import redirect
from django.urls import reverse

class RestrictedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_url = request.path_info

        exempt_urls = [
            reverse('landing_page:index'), 
            reverse('login'), 
        ]

        if not request.user.is_authenticated and current_url not in exempt_urls:
            return redirect(reverse('login'))
        
        if request.user.is_authenticated and current_url == reverse('login'):
            return redirect(reverse('home:index'))

        response = self.get_response(request)
        return response
