from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse

from ..models import Profile


class CustomLoginView(LoginView):
    """
        A custom class to login straight to user profile using pk
    """

    def check_user_profile_partially_complete(self):
        account_id = self.request.user.id
        user_profile = Profile.objects.get(id=account_id)
        return user_profile.is_partially_complete

    def get_success_url(self):
        url = self.get_redirect_url()
        if self.check_user_profile_partially_complete():
            return url or reverse('user:profile-detail', kwargs={'pk': self.request.user.id})
        else:
            return url or reverse('user:edit-profile', kwargs={'pk': self.request.user.id})
