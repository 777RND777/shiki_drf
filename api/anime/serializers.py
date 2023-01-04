from rest_framework.serializers import ModelSerializer

from . import models


class AnimeSerializer(ModelSerializer):
    class Meta:
        model = models.Anime
        fields = '__all__'
