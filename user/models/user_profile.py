from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    middle_names = models.CharField(max_length=128)
    locality = models.CharField(max_length=30, null=True)

    # def __str__(self):
    #     return str(f"{self.last_name}, {self.last_name}")

    def __str__(self):
        return str(f"{self.pk}")