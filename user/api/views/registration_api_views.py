from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import UserSerializer

User = get_user_model()

class RegisterApiView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)


class LoginApiView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User could not be found.')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect username or password.')

        return Response({"message": "Successfully logged in"})

