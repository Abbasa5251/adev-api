from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api.serializers import ContactSerializer


@swagger_auto_schema(
    tags=["Contact"],
    method="POST",
    operation_id="Create Contact",
    operation_description="Create a contact",
    responses={201: ContactSerializer},
    request_body=ContactSerializer,
)
@api_view(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        contact = request.data
        serializer = ContactSerializer(data=contact)
        if serializer.is_valid():
            serializer.save()
            formatted_response = {"status": status.HTTP_201_CREATED, "contact": serializer.data}
            return Response(formatted_response, status=status.HTTP_201_CREATED)

        formatted_response = {"status": status.HTTP_400_BAD_REQUEST, "error": serializer.errors}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
