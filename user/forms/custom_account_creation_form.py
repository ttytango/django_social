from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ..models import Account


class CustomUserCreationForm(UserCreationForm):

    confirm_email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['email', 'confirm_email', ]

    def clean_confirm_email(self):
        email = self.cleaned_data['email']
        confirm_email = self.cleaned_data['confirm_email']
        if email == confirm_email:
            return email
        else:
            raise ValidationError(_('The emails provided do not match.'))
