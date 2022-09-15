from common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Skill(TimeStampedUUIDModel):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.CharField(max_length=255, verbose_name=_("description"))

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")
        ordering = ("-created_at", "-updated_at")

    def __str__(self):
        return self.name
