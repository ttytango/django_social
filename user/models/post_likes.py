from django.utils.translation import gettext_lazy as _
from django.db import models

from ..models import Profile, Post


class PostLikes(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    date_liked = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')
