from rest_framework import serializers

from . import models


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    anime_title = serializers.CharField(source='anime.title')

    class Meta:
        model = models.Review
        fields = ['score', 'text', 'anime_title']

