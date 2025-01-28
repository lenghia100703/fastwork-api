from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string

from libs.models import BaseModel
from libs.utils import get_random_digit_code

from .user import User


class UserVerificationCode(BaseModel):
    CODE_LENGTH = 5
    TOKEN_LENGTH = 32
    EXPIRE_TIME = 300  # seconds

    # normal fields
    code = models.CharField(max_length=CODE_LENGTH)
    code_expires_at = models.DateTimeField()
    verification_token = models.CharField(
        max_length=TOKEN_LENGTH, null=True, blank=True
    )
    verification_token_expires_at = models.DateTimeField(null=True, blank=True)

    # relational fields
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="verification_codes"
    )

    class Meta:
        ordering = ("-code_expires_at",)
        unique_together = ("user", "code")

    def __str__(self) -> str:
        return f"Verification code for user with email {self.user.email}"

    # region: class methods
    @classmethod
    def for_user(cls, user: User) -> "UserVerificationCode":
        return cls.objects.create(
            user=user,
            code=get_random_digit_code(cls.CODE_LENGTH),
            code_expires_at=timezone.now()
            + timezone.timedelta(seconds=cls.EXPIRE_TIME),
        )

    # endregion: class methods

    # region: properties
    @property
    def is_latest(self) -> bool:
        """
        Check if the current instance is the latest verification code for the user.
        If not, then it should not be used for validation.
        Therefore, it should be considered as expired and user need to request for a
        new code to use.
        """
        latest = self.user.verification_codes.first()
        return self == latest

    @property
    def is_code_expired(self) -> bool:
        return timezone.now() > self.code_expires_at or not self.is_latest

    @property
    def is_verification_token_expired(self) -> bool:
        return (
            timezone.now() > self.verification_token_expires_at
            or not self.is_latest
        )

    # endregion: properties

    # region: instance methods
    def update_verification_token(self):
        """
        Update the verification token and its expiration time.
        """
        self.verification_token = get_random_string(self.TOKEN_LENGTH)
        self.verification_token_expires_at = (
            timezone.now() + timezone.timedelta(seconds=self.EXPIRE_TIME)
        )
        self.save(
            update_fields=[
                "verification_token",
                "verification_token_expires_at",
            ]
        )

    # endregion: instance methods