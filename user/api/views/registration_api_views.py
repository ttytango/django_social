from datetime import datetime, timedelta

import jwt
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers import UserSerializer

User = get_user_model()

class RegisterApiView(APIView):

    def post(self, request):
        print(request.data)
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

        payload = {
            "id": user.id,
            "exp": datetime.utcnow() + timedelta(seconds=3600),
            "iat": datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.data = {
            "jwt": token
        }
        response.set_cookie(key='jwt', value=token, httponly=True)

        return response


class UserApiView(APIView):

    def get(self, request):
        token = request.COOKIES['jwt']
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "message": "Logged out"
        }
        return response