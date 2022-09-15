from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.utils.decorators import method_decorator

from .api.serializers import ProjectSerializer, TagSerializer
from .models import Project, Tag


class ProjectListView(generics.GenericAPIView):
    serializer_class = ProjectSerializer

    @method_decorator(
        name="get",
        decorator=swagger_auto_schema(
            operation_id="Projects List", operation_description="List all projects"
        ),
    )
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        serializer = self.serializer_class(projects, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)


class TagListView(generics.GenericAPIView):
    serializer_class = TagSerializer

    @method_decorator(
        name="get",
        decorator=swagger_auto_schema(
            operation_id="Tags List", operation_description="List all tags"
        ),
    )
    def get(self, request, *args, **kwargs):
        tags = Tag.objects.all()
        serializer = self.serializer_class(tags, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=["Projects"],
    method="GET",
    operation_id="Projects List",
    operation_description="List all projects",
    responses={200: ProjectSerializer},
)
@api_view(["GET"])
def projects_list(request):
    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=["Projects"],
    method="GET",
    operation_id="Tags List",
    operation_description="List all tags",
    responses={200: TagSerializer},
)
@api_view(["GET"])
def tags_list(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        return Response(formatted_response, status=status.HTTP_200_OK)
