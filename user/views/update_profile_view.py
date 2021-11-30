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
    # success_url = reverse_lazy('user:profile-detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Edit Profile")
        context['email'] = self.request.user.email
        return context

    def post(self, request, **kwargs):
        request = self.request
        self.object = self.get_object()
        print(request.POST)
        # request.POST = request.POST.copy()
        # request.POST['description'] = self.object.description
        # request.POST['season'] = 2
        return super().post(request, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     super().post(self, request, *args, **kwargs)
    #     print(self.request.POST)
    #     return self.form_valid(self)
    #
    #     # print(self.cleaned_data)

    def get_success_url(self):
        return reverse_lazy('user:profile-detail', kwargs = {'pk': self.request.user.id})
