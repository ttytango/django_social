from django.db import models

from ..models import Profile


class FriendRequest(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='from_user', on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, related_name='to_user', on_delete=models.CASCADE)
    date_time_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.from_profile.user}, {self.to_profile.user}")
