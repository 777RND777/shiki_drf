from django.http import Http404

from .models import Anime


def get_anime_by_slug(slug):
    try:
        return Anime.objects.get(slug=slug)
    except Anime.DoesNotExist:
        raise Http404
