from rest_framework import permissions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ...models import Profile
from ..serializers import ProfileSerializer


class ListProfiles(generics.ListCreateAPIView):
    """
    View to list all users in the system.
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication] TODO: * Requires token authentication.
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [permissions.IsAdminUser] # TODO: permissions

class RetrieveProfile(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_fields = ['user']