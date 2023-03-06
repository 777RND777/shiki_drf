from rest_framework import serializers

from . import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name',)


class AnimeSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = models.Anime
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    anime_title = serializers.CharField(source='anime.title', required=False)
    anime_episodes = serializers.IntegerField(source='anime.episodes', required=False)

    class Meta:
        model = models.Review
        fields = ('anime_title', 'status', 'score', 'watched_episodes', 'anime_episodes', 'text')
