from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from . import models, serializers


@api_view()
def main_page(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = models.Anime.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = serializers.AnimeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
