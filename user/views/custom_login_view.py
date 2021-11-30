from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from ..models import Profile


class CustomLoginView(LoginView):
    """
        A custom class to login straight to user profile using pk
    """

    template_name = "user/forms/auth_form.html"

    def check_user_profile_partially_complete(self):
        """
        Check to see if user has at least added their
        first and last names to their profile
        :return: True if the user has started their profile
        """
        account_id = self.request.user.id
        user_profile = Profile.objects.get(id=account_id)
        return user_profile.is_partially_complete

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Login")
        context['form_title'] = _("Login")
        context['forgot_password'] = True
        return context

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
