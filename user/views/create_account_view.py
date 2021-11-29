from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..forms import CustomUserCreationForm

Account = get_user_model()

class CreateAccountView(CreateView):

    form_class = CustomUserCreationForm
    template_name = "user/registration/register.html"
    model = Account
    success_url = reverse_lazy('index')

