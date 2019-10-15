from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddelware:

    def __init__(self , get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            user = request.user
            if not hasattr(user, 'profiles'):
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response
