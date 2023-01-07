from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import services
from anime import models as anime_models
from anime import serializers as anime_serializers
from users import models as user_models
from users import serializers as user_serializers

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@api_view()
@cache_page(CACHE_TTL)
def get_user_detail(request, slug):
    user = get_object_or_404(user_models.User, slug=slug)
    serializer = user_serializers.UserSerializer(user)
    return Response(serializer.data)


@api_view()
@cache_page(CACHE_TTL)
def get_review_list(request, slug, status: str = ""):
    if len(status) > 0 and status not in anime_models.Review.Status:
        return redirect(get_review_list, slug)

    review_objects = services.get_user_reviews(slug, status)
    serializer = anime_serializers.ReviewSerializer(review_objects, many=True)
    return Response(serializer.data)
