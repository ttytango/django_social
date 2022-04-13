from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from ..permissions import IsOwner
from ...models import Profile
from ..serializers import ProfileSerializer, ProfileCreateSerializer


class ListProfiles(generics.ListCreateAPIView):
    """
    View to list all users in the system.
    """
    permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RetrieveProfile(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CreatePatchProfileView(APIView):
    permission_classes = [IsOwner]
    http_method_names = ['get', 'patch',]
    queryset = Profile.objects.all()
    serializer_class = ProfileCreateSerializer

    def get_object(self, pk):
        try:
            return Profile.objects.get(user_id=pk)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        profile = self.get_object(pk)
        serializer = ProfileCreateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



