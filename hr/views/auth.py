from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenBlacklistView,
    TokenRefreshView,
)

from ..serializers import SignUpConfirmSerializer, SignUpSerializer


class LoginAPIView(TokenObtainPairView):
    http_method_names = ["post"]


class LogoutAPIView(TokenBlacklistView):
    http_method_names = ["post"]


class SignUpAPIView(APIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer

    @extend_schema(
        responses={
            200: inline_serializer(
                name="SignUp",
                fields={
                    "user_id": serializers.IntegerField(),
                    "refresh": serializers.CharField(),
                    "access": serializers.CharField(),
                },
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpConfirmAPIView(APIView):
    http_method_names = ["post"]
    permission_classes = [AllowAny]
    serializer_class = SignUpConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response(token, status=status.HTTP_200_OK)


class UserRefreshTokenAPIView(TokenRefreshView):
    http_method_names = ["post"]
