from phonenumber_field.modelfields import PhoneNumberField

from common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class About(TimeStampedUUIDModel):
    description = models.TextField(verbose_name=_("description"))
    address = models.TextField(verbose_name=_("address"))
    city = models.CharField(max_length=64, verbose_name=_("city"))
    email = models.EmailField(verbose_name=_("email"))
    phone_number = PhoneNumberField(
        max_length=14, verbose_name=_("phone number"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
