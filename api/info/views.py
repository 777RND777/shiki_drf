from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import services
from users import serializers


@api_view()
def get_user_detail(request, slug):
    user = services.get_user_by_slug(slug)
    serializer = serializers.UserSerializer(user)
    return Response(serializer.data)
