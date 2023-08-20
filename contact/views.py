import logging

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api.serializers import ContactSerializer

logger = logging.getLogger(__name__)


@api_view(["POST"])
def contact(request):
    if request.method == "POST":
        contact = request.data
        serializer = ContactSerializer(data=contact)
        if serializer.is_valid():
            serializer.save()
            formatted_response = {"status": status.HTTP_201_CREATED, "data": serializer.data}
            logger.info(f"POST:/api/v1/contact:Contact request created : {request.user}")
            return Response(formatted_response, status=status.HTTP_201_CREATED)

        formatted_response = {"status": status.HTTP_400_BAD_REQUEST, "error": serializer.errors}
        logger.error(f"POST:/api/v1/contact:There was an error creating contact : {request.user}")
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)
