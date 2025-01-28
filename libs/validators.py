from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class PasswordValidator(RegexValidator):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"  # noqa
    message = _(
        "Password must be least 8 characters, with at least one uppercase, "
        "one lowercase, one digit, one special character, and no spaces."
    )
    code = "invalid_password"


class PhoneNumberValidator(RegexValidator):
    regex = "^(0)(3[2-9]|5[2-9]|7[0-9]|8[1-9]|9[0-9])[0-9]{7}$"
    message = _(
        "Phone number must be 10 digits."
    )
    code = "invalid_phone_number"