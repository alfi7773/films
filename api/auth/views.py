from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from api.auth.serializers import LoginSerializer, ReadUserSerializer


class LoginApiView(APIView):
    

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username, password = serializer.validated_data.get('username'), serializer.validated_data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            read_serializer = ReadUserSerializer(user, context={'request': request})

            data = {
                **read_serializer.data,
                'token': token.key
            }

            return Response(data)

        return Response({'detail': 'Пользователь не найден или не правильный пароль.'}, status.HTTP_400_BAD_REQUEST)