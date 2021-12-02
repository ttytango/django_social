from django import forms
from django.forms import ModelForm
from ..models import Profile, Expertise


class ProfileEditForm(ModelForm):

    expertise = forms.ModelMultipleChoiceField(
        queryset=Expertise.objects.none(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'middle_names', 'locality', 'profile_image', 'expertise', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['middle_names'].required = False
        self.fields['profile_image'].required = False
        self.fields['expertise'].required = False
        self.fields['expertise'].queryset = Expertise.objects.all()
        self.fields['expertise'].initial = None



