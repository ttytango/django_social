from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from ..models import Profile


class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'user/account/user_profile.html'
    model = Profile
    context_object_name = 'profile'

    # def get_object(self):
    #     return self.model.objects.get(id=self.request.user.id)

