from django.shortcuts import redirect
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
def get_review_list(request, slug, status: str = ""):
    if len(status) > 0 and status not in anime_models.Review.Status:
        return redirect(get_review_list, slug)

    review_objects = services.get_user_reviews(slug, status)
    serializer = anime_serializers.ReviewSerializer(review_objects, many=True)
    return Response(serializer.data)
