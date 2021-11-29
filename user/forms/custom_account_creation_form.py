from django.contrib.auth.forms import UserCreationForm

from ..models import Account


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email',)

