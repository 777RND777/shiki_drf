from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


@api_view()
@permission_classes([IsAuthenticated])
def main_page(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = models.Anime.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = serializers.AnimeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
