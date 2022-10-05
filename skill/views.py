import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api.serializers import SkillSerializer
from .models import Skill

logger = logging.getLogger(__name__)


@swagger_auto_schema(
    tags=["Skill"],
    method="GET",
    operation_id="Skills List",
    operation_description="List all skills",
    responses={200: SkillSerializer(many=True)},
)
@api_view(["GET"])
def skills_list(request):
    if request.method == "GET":
        projects = Skill.objects.all()
        serializer = SkillSerializer(projects, many=True, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "result": serializer.data}
        logger.info(f"GET:/api/v1/skills : {request.user}")
        return Response(formatted_response, status=status.HTTP_200_OK)


@swagger_auto_schema(
    tags=["Skill"],
    method="GET",
    operation_id="Skill Detail",
    operation_description="Get skill detail",
    parameters=openapi.Parameter(
        "id",
        openapi.IN_QUERY,
        description="UUID for skill to get detail",
        type=openapi.TYPE_STRING,
    ),
    responses={200: SkillSerializer()},
)
@api_view(["GET"])
def skill_detail(request, id):
    if request.method == "GET":
        project = Skill.objects.filter(id=id).first()
        serializer = SkillSerializer(project, context={"request": request})
        formatted_response = {"status": status.HTTP_200_OK, "result": serializer.data}
        logger.info(f"GET:/api/v1/skills/{id} : {request.user}")
        return Response(formatted_response, status=status.HTTP_200_OK)
