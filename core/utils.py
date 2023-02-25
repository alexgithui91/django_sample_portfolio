from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def send_inquiry_email(
    request,
    mail_subject,
    email_template,
    message,
    full_name,
    email,
):
    from_email = settings.EMAIL_HOST_USER
    message = render_to_string(
        email_template,
        {"full_name": full_name, "message": message, "email": email},
    )

    to_email = settings.EMAIL_HOST_USER
    mail = EmailMessage(
        mail_subject,
        message,
        from_email,
        to=[to_email],
    )
    mail.send()
