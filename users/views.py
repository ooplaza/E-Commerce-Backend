from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model


# Create your views here.
class CustomUserRegister(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        register_serializer = UserSerializer(data=request.data)
        if register_serializer.is_valid(raise_exception=True):
            new_user = register_serializer.save()
            if new_user:
                # If successful
                return Response(data=register_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLogout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as error:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CustomUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve the user associated with the current request
        user = request.user

        # Serialize the user data using your UserSerializer
        user_serializer = UserSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)