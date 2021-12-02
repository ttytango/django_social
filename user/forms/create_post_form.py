from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from ..models import Post


class PostCreateForm(ModelForm):
    #
    # content = forms.CharField(
    #     widget=forms.Textarea(),
    # )

    class Meta:
        model = Post
        fields = ('content', )

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['content'] = forms.CharField()
        self.fields['content'].widget = forms.Textarea()
        self.fields['content'].label = _("Be creative")
        self.fields['content'].widget.attrs.update({
                'placeholder': _("Write something here..."),
                'cols': 40,
                'rows': 10,
            }
        )


