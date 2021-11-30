from django import forms
from django.forms import ModelForm
from ..models import Profile

class ProfileEditForm(ModelForm):


    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'middle_names', 'locality', 'profile_image', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['middle_names'].required = False
        self.fields['profile_image'].required = False

    # def __init__(self, *args, **kwargs):
    #     form = super(ProfileEditForm, self).__init__(*args, **kwargs)
    #     form['email'] = self.request.user.id
    #     for index in range(int(nb_dogs)):
    #         self.fields.update({
    #             'dog_%s_name' % index: forms.CharField(label=_('Name'), required=False, max_length=512),
    #         })
