from django.contrib import admin

from .models import Skill


class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "pkid", "id")
    list_filter = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_display_links = ("id", "pkid")


admin.site.register(Skill, SkillAdmin)
