from common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class About(TimeStampedUUIDModel):
    description = models.TextField(verbose_name=_("description"))

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
