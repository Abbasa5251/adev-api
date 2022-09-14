from rest_framework import generics, status
from rest_framework.response import Response

from .api.serializers import ProjectSerializer
from .models import Project


class ProjectListView(generics.GenericAPIView):
    serializer_class = ProjectSerializer

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = ProjectSerializer(
            projects, many=True, context={"request": request}
        )
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)
