from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, services, serializers


@api_view()
def get_anime_list(request, genre: str = "", studio: str = ""):
    if len(genre) > 0 and models.Genre.objects.filter(name=genre).first() is None:
        return redirect(get_anime_list)
    if len(studio) > 0 and models.Studio.objects.filter(name=genre).first() is None:
        return redirect(get_anime_list)

    paginator = PageNumberPagination()
    paginator.page_size = 20
    anime_objects = services.get_anime_list(genre, studio)
    result_page = paginator.paginate_queryset(anime_objects, request)
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
