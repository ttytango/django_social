from rest_framework import serializers
from ...models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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

        read_only_fields = ['user', ]

class ProfileCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'middle_names',
            'locality',
            'profile_image',
            'user'
        ]

        read_only_fields = ['user', ]

