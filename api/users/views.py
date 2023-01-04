from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers, services


@api_view(["POST"])
def sign_up(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    serializer.instance = services.create_user(data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
