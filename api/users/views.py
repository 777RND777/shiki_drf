from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models, serializers, services

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view()
@cache_page(CACHE_TTL)
def get_user_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    user_objects = models.User.objects.filter(is_superuser=False)
    result_page = paginator.paginate_queryset(user_objects, request)
    serializer = serializers.UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
def sign_up(request):
    serializer = serializers.RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    data = serializer.validated_data
    serializer.instance = services.create_user(data)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
