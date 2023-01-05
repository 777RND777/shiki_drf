from rest_framework.serializers import ModelSerializer

from . import models


class AnimeSerializer(ModelSerializer):
    class Meta:
        model = models.Anime
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['score', 'text']
