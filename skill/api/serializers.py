from rest_framework import serializers

from skill.models import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = (
            "id",
            "name",
            "description",
            "proficiency",
        )
        read_only_fields = ("id",)
