from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, services, serializers

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view()
@cache_page(CACHE_TTL)
def get_anime_list(request, *args, **kwargs):
    if 'kind' in kwargs and kwargs['kind'] not in models.Anime.Kind:
        return redirect(get_anime_list)
    if 'status' in kwargs and kwargs['status'] not in models.Anime.Status:
        return redirect(get_anime_list)
    if 'genre' in kwargs and models.Genre.objects.filter(slug=kwargs['genre']).first() is None:
        return redirect(get_anime_list)
    if 'studio' in kwargs and models.Studio.objects.filter(slug=kwargs['studio']).first() is None:
        return redirect(get_anime_list)

    paginator = PageNumberPagination()
    paginator.page_size = 20
    anime_objects = services.get_anime_list(kwargs)
    result_page = paginator.paginate_queryset(anime_objects, request)
    serializer = serializers.AnimeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view()
@cache_page(CACHE_TTL)
def get_anime_detail(request, slug):
    anime = get_object_or_404(models.Anime, slug=slug)
    serializer = serializers.AnimeSerializer(anime)
    return Response(serializer.data)


@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def review_anime(request, slug):
    anime = get_object_or_404(models.Anime, slug=slug)
    serializer = serializers.ReviewSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    with transaction.atomic():
        review = services.create_review(data, request.user.pk, anime.pk)
        if 'score' in data:
            services.update_anime_score(data['score'], anime)
    return Response(serializers.ReviewSerializer(instance=review).data)
