from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from .expertise import Expertise

Account = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_names = models.CharField(max_length=128, blank=True)
    locality = models.CharField(max_length=30, null=True)
    profile_image = models.ImageField(upload_to='users/profile_images/', null=True, blank=True)
    friends = models.ManyToManyField("Profile", blank=True)
    expertise = models.ManyToManyField(Expertise, related_name='users')

    def __str__(self):
        return str(f"{self.last_name}, {self.first_name}")

    @property
    def photo_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url

    @property
    def is_partially_complete(self):
        if self.first_name and self.last_name:
            return True
        else:
            return False

    @property
    def email(self):
        user = Account.objects.get(id=self.id)
        return user.email

