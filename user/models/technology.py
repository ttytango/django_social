from django.db import models
from django.utils.translation import ugettext_lazy as _

class Technology(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = _("technologies")

    def __str__(self):
        return self.name
