from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_names = models.CharField(max_length=128, blank=True)
    locality = models.CharField(max_length=30, null=True)
    profile_image = models.ImageField(upload_to='users/profile_images/', null=True, blank=True)

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

    #
    # def get_absolute_url(self):
    #     return reverse('user:profile-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs): # new
    #     if not self.slug:
    #         self.slug = slugify(str(f"{self.first_name} {self.last_name}"))
    #     return super().save(*args, **kwargs)
