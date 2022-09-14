from rest_framework import serializers

from project.models import Project, Tag


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "pkid",
            "id",
            "title",
            "slug",
            "description",
            "body",
            "image",
            "source_link",
            "demo_link",
        )
        read_only_fields = ("pkid", "id")

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("pkid", "id", "name", "created_at", "updated_at")
        read_only_fields = ("pkid", "id")
