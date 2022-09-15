from rest_framework import generics, status
from rest_framework.response import Response

from .api.serializers import ProjectSerializer, TagSerializer
from .models import Project, Tag


class ProjectListView(generics.GenericAPIView):
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = self.serializer_class(
            projects, many=True, context={"request": request}
        )
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)

class TagListView(generics.GenericAPIView):
    serializer_class = TagSerializer

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = self.serializer_class(
            tags, many=True, context={"request": request}
        )
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)
