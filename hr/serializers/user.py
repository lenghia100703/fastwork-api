from rest_framework import serializers
from rest_framework.fields import EmailField
from rest_framework.serializers import ModelSerializer

from hr.models import User
from libs.validators import PhoneNumberValidator


class UserSerializer(ModelSerializer):
    email = EmailField(read_only=True)
    phone_number = serializers.CharField(
        allow_blank=True,
        allow_null=True,
        max_length=20,
        required=False,
        validators=[PhoneNumberValidator()],
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "avatar",
            "role",
            "email_verified",
        ]
