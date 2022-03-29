from rest_framework import serializers
from ...models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'first_name',
            'last_name',
            'middle_names',
            'locality',
            'profile_image',
            'friends',
            'expertise',
        ]

