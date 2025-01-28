from typing import Dict

from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken

from libs.validators import PasswordValidator, PhoneNumberValidator

from ..models import User


class SignUpMixin:
    def get_tokens_for_user(self, user: User) -> Dict[str, str]:
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class SignUpSerializer(SignUpMixin, serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField(validators=[PasswordValidator()])
    password2 = serializers.CharField(validators=[PasswordValidator()])
    phone_number = serializers.CharField(
        max_length=20,
        required=False,
        allow_blank=True,
        validators=[PhoneNumberValidator()],
    )

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_password1(self, value):
        validate_password(value)
        return value

    def validate_password2(self, value):
        validate_password(value)
        return value

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        validate_password(attrs["password1"])
        return attrs

    def create(self, validated_data):
        phone_number = validated_data.get("phone_number", "")
        instance = User(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            phone_number=phone_number,
            is_active=True,
        )
        instance.set_password(validated_data["password1"])
        instance.save()
        return instance

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        tokens = self.get_tokens_for_user(self.instance)
        update_last_login(None, self.instance)
        data = {"user_id": self.instance.id, **tokens}
        return data


class SignUpConfirmSerializer(SignUpMixin, serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    refresh = serializers.CharField(required=False, read_only=True)
    access = serializers.CharField(required=False, read_only=True)

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        # Decode the uidb64 (allauth use base36) to uid to get User object
        try:
            uid = force_str(uid_decoder(attrs["uid"]))
            self.user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            raise ValidationError({"uid": [_("Invalid value")]})

        if not default_token_generator.check_token(self.user, attrs["token"]):
            raise ValidationError({"token": [_("Invalid value")]})

        self.custom_validation(attrs)
        return attrs

    def save(self):
        self.user.email_verified = True
        self.user.save(update_fields=["email_verified"])
        tokens = self.get_tokens_for_user(self.user)
        update_last_login(None, self.user)
        return tokens
