from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_anime(request, slug):
    anime = services.get_anime_by_slug(slug)
    serializer = serializers.ReviewSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    review = services.create_review(data, request.user.pk, anime.pk)
    services.update_anime_score(data.get('score', review.score), anime)
    return Response({"message": "OK"})
