from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models, serializers, services


@api_view()
def get_user_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = models.User.objects.filter(is_superuser=False)
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = serializers.UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
def sign_up(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    serializer.instance = services.create_user(data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
