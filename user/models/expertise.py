from django.db import models
from django.utils.translation import gettext_lazy as _
from .technology import Technology

class Expertise(models.Model):

    LEVEL_CURIOUS = 1
    LEVEL_BEGINNER = 2
    LEVEL_INTERMEDIATE = 3
    LEVEL_ADVANCED = 4
    LEVEL_GOAT = 5

    LEVEL_CHOICES = [
       (LEVEL_CURIOUS, _("Curious")),
       (LEVEL_BEGINNER, _("Beginner")),
       (LEVEL_INTERMEDIATE, _("Semi-Professional")),
       (LEVEL_ADVANCED, _("Professional")),
       (LEVEL_GOAT, _("Exceptional")),
    ]

    level = models.IntegerField(choices=LEVEL_CHOICES, default=LEVEL_BEGINNER)

    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)

    date_started = models.DateField()


    def __str__(self):
        return str(f"{self.technology}")



    class Meta:
        verbose_name_plural = _("expertise")
