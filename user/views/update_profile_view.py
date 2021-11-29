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
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.model.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data (**kwargs)
        context['title'] = _("Edit Profile")
        context['email'] = self.request.user
        return context



