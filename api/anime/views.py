from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import models, services, serializers


@api_view()
def get_anime_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    person_objects = models.Anime.objects.all()
    result_page = paginator.paginate_queryset(person_objects, request)
    serializer = serializers.AnimeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view()
def get_anime_detail(request, slug):
    anime = services.get_anime_by_slug(slug)
    serializer = serializers.AnimeSerializer(anime)
    return Response(serializer.data)
