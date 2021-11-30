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
        """
        Check to see if user has at least added their
        first and last names to their profile
        :return: True if the user has started their profile
        """
        account_id = self.request.user.id
        user_profile = Profile.objects.get(id=account_id)
        return user_profile.is_partially_complete

    def get_success_url(self):
        """
        On login user is redirected to edit profile if they need
        to add to their profile or their main profile page
        """
        url = self.get_redirect_url()
        if self.check_user_profile_partially_complete():
            return url or reverse('user:profile-detail', kwargs={'pk': self.request.user.id})
        else:
            return url or reverse('user:edit-profile', kwargs={'pk': self.request.user.id})
