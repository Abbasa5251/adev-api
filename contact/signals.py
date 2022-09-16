from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Contact


@receiver(post_save, sender=Contact)
def contact_send_mail(sender, instance, created, **kwargs):
    if created:
        contact = instance
        user_subject = "Thank you for contacting ADev Tutorials"
        user_message = "We will get back to you as soon as possible."
        send_mail(
            user_subject,
            user_message,
            settings.DEFAULT_EMAIL,
            [contact.email],
            fail_silently=True,
        )
        subject = "Someone is trying to contact on ADev Tutorials"
        message = f"There is a email from {contact.name} {contact.email}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_EMAIL,
            [settings.DEFAULT_EMAIL],
            fail_silently=True,
        )


post_save.connect(contact_send_mail, sender=Contact)
