from phonenumber_field.modelfields import PhoneNumberField

from common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(TimeStampedUUIDModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    phone_number = PhoneNumberField(
        max_length=14, verbose_name=_("phone number"), null=True, blank=True
    )
    subject = models.CharField(max_length=100, verbose_name=_("subject"))
    message = models.TextField(verbose_name=_("message"))

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return f"{self.name} {self.email}"
