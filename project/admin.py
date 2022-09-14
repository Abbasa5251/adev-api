from django.contrib import admin

from .models import Project, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "pkid",
        "id",
        "title",
        "slug",
        "image",
        "source_link",
        "demo_link",
    )
    list_filter = ("title", "created_at", "updated_at")
    search_fields = ("title", "description", "body")
    list_display_links = ("id", "pkid")


admin.site.register(Project, ProjectAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ("pkid", "id", "name")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_display_links = ("id", "pkid")


admin.site.register(Tag, TagAdmin)
