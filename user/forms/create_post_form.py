from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from ..models import Post


class PostCreateForm(ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(),
    )

    class Meta:
        model = Post
        fields = ('content', )
        labels = {'content': _("Write some content to publish")}

