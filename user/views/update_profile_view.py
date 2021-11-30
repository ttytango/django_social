from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.utils.translation import gettext_lazy as _

from ..forms import ProfileEditForm
from ..models import Profile


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileEditForm
    model = Profile
    template_name = 'user/account/edit_profile.html'
    success_message = _('Your profile has been successfully updated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Edit Profile")
        context['email'] = self.request.user.email
        return context

    def get_success_url(self):
        return reverse_lazy('user:profile-detail', kwargs={'pk': self.request.user.id})
