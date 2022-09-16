from autoslug import AutoSlugField

from common.models import TimeStampedUUIDModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(TimeStampedUUIDModel):
    title = models.CharField(max_length=100, verbose_name=_("title"))
    slug = AutoSlugField(
        populate_from="title", unique=True, verbose_name=_("slug"), always_update=True
    )
    description = models.CharField(max_length=255, verbose_name=_("description"))
    body = models.TextField(verbose_name=_("body"), blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="projects", blank=True)
    image = models.ImageField(
        verbose_name=_("image"),
        blank=True,
        upload_to="images/",
        default="images/default.jpg",
    )
    source_link = models.CharField(
        max_length=128, verbose_name=_("source code"), blank=True, null=True
    )
    demo_link = models.CharField(max_length=128, verbose_name=_("demo link"), blank=True, null=True)

    class Meta:
        verbose_name = _("project")
        verbose_name_plural = _("projects")
        ordering = ("-created_at", "-updated_at")

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        try:
            url = self.image.url
        except Exception:
            url = ""
        return url


class Tag(TimeStampedUUIDModel):
    name = models.CharField(max_length=128, verbose_name=_("name"), unique=True)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        ordering = ("-created_at", "-updated_at")

    def __str__(self):
        return self.name
