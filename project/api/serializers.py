from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers

from project.models import Project, Tag


class TagsListSerializerField(serializers.ListField):
    child = serializers.CharField()


class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "body",
            "tags",
            "image",
            "source_link",
            "demo_link",
        )
        read_only_fields = ("id",)

    @swagger_serializer_method(serializer_or_field=serializers.URLField)
    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_url)

    @swagger_serializer_method(serializer_or_field=TagsListSerializerField)
    def get_tags(self, obj):
        _tags = obj.tags.all()
        return [tag.name for tag in _tags]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "created_at", "updated_at")
        read_only_fields = ("id",)
