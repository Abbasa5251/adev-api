from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import get_template

from .models import Contact


@receiver(post_save, sender=Contact)
def contact_send_mail(sender, instance, created, **kwargs):
    if created:
        contact = instance
        user_subject = "Thank you for contacting ADev Tutorials"
        html_message = get_template("contact/email.html")
        message = html_message.render({"user_name": contact.name})
        send_mail(
            user_subject,
            message,
            settings.DEFAULT_EMAIL,
            [contact.email],
            fail_silently=False,
        )
        subject = "Someone is trying to contact on ADev Tutorials"
        message = f"There is a email from {contact.name} {contact.email}"
        send_mail(
            subject,
            message,
            settings.DEFAULT_EMAIL,
            [settings.DEFAULT_EMAIL],
            fail_silently=False,
        )


post_save.connect(contact_send_mail, sender=Contact)
