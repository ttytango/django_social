from django.contrib.auth.forms import UserChangeForm
from ..models import Account


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email',)
