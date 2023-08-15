import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .api.serializers import ProjectDetailSerializer, ProjectSerializer, TagSerializer
from .models import Project, Tag

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    tags=["Project"],
    method="GET",
    operation_id="Projects List",
    operation_description="List all projects",
    responses={200: ProjectSerializer(many=True)},
)
@api_view(["GET"])
def projects_list(request):
    if request.method == "GET":
        paginator = PageNumberPagination()
        paginator.page_size = 5
        projects = Project.objects.all()
        projects = paginator.paginate_queryset(projects, request)
        serializer = ProjectSerializer(projects, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        logger.info(f"GET:/api/v1/projects : {request.user}")
        return Response(formatted_response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=["Project"],
    method="GET",
    operation_id="Project Detail",
    operation_description="Get project detail",
    parameters=openapi.Parameter(
        "id",
        openapi.IN_QUERY,
        description="UUID for project to get detail",
        type=openapi.TYPE_STRING,
    ),
    responses={200: ProjectDetailSerializer()},
)
@api_view(["GET"])
def project_detail(request, id):
    if request.method == "GET":
        project = Project.objects.filter(id=id).first()
        serializer = ProjectDetailSerializer(project, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "data": serializer.data}
        logger.info(f"GET:/api/v1/projects/{id} : {request.user}")
        return Response(formatted_response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=["Tag"],
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
        logger.info(f"GET:/api/v1/projects/tags : {request.user}")
        return Response(formatted_response, status=status.HTTP_200_OK)
