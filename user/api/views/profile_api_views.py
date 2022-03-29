from rest_framework import permissions, authentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import Profile
from ..serializers import ProfileSerializer


class ListProfiles(generics.ListCreateAPIView):
    """
    View to list all users in the system.
    """
    # permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RetrieveProfile(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_fields = ['user']