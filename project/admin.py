from django.contrib import admin

from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("pkid", "id", "title", "slug", "image", "source_link", "demo_link")
    list_filter = ("title", "created_at", "updated_at")
    search_fields = ("title", "description", "body")
    list_display_links = ("id", "pkid")


admin.site.register(Project, ProjectAdmin)
