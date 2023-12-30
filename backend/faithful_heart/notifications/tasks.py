from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from notifications.models import EmailNewsletter
from users.models import TelegramUser

from faithful_heart.constants import EMAIL_ADDRESS


@shared_task
def check_and_send_newsletters():
    newsletters = EmailNewsletter.objects.filter(
        is_finished=False,
        sending_date=timezone.now()
    )
    recipients = list(
        TelegramUser.objects.filter(
            email__isnull=False
        ).values_list(
            "email", flat=True
        )
    )
    for newsletter in newsletters:
        send_mail(
            newsletter.subject,
            newsletter.message,
            EMAIL_ADDRESS,
            [recipients],
            fail_silently=False,
        )
        newsletter.sent = True
        newsletter.save()
