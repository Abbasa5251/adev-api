from rest_framework import serializers


class TagsListSerializerField(serializers.ListField):
    child = serializers.CharField()
