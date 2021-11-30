from django.contrib import messages
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms import CustomUserCreationForm
from django.utils.translation import gettext_lazy as _

Account = get_user_model()

class CreateAccountView(CreateView):

    form_class = CustomUserCreationForm
    template_name = "user/forms/auth_form.html"
    model = Account
    success_url = reverse_lazy('user:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Sign Up")
        context['form_title'] = _("Registration")
        return context

    def form_valid(self, form):
        messages.success(self.request, _('Your account has been created, please log in!'))
        return super().form_valid(form)


