import logging

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from fastwork.celery_tasks import app
from hr.models import User

logger = logging.getLogger(__name__)


@app.task()
def send_successful_signup_email(user_id: int) -> int:
    logger.info(f"Sending successful signup email to User #{user_id}")
    email_template = "email_templates/hr/successfully_signup.html"

    user = User.objects.filter(id=user_id).first()
    if not user:
        logger.error(f"User with id {user_id} not found")
        return

    context = {
        "user_name": user.get_full_name(),
        "settings": settings,
        "user": user,
    }

    if not user.email_verified:
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        url = f"{settings.FRONTEND_URL}/registration/confirm?uid={uid}&token={token}"
        context["url"] = url

    html_message = render_to_string(email_template, context)
    from_email = settings.EMAIL_SENDER
    logger.info(f"Sending signup mail to user with email: {user.email}")
    logger.info(f"HTML Message: \n{html_message}")
    return send_mail(
        "Fastwork: registration confirmation",
        "",
        from_email=from_email,
        recipient_list=[user.email],
        html_message=html_message,
    )
