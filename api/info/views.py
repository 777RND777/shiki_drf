from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import services
from anime import models as anime_models
from anime import serializers as anime_serializers
from users import serializers as user_serializers


@api_view()
def get_user_detail(request, slug):
    user = services.get_user_by_slug(slug)
    serializer = user_serializers.UserSerializer(user)
    return Response(serializer.data)


@api_view()
def get_review_list(request, slug):
    user = services.get_user_by_slug(slug)
    reviews = anime_models.Review.objects.filter(user_id=user.pk).select_related()
    serializer = anime_serializers.ReviewSerializer(reviews, many=True)
    return Response(serializer.data)
