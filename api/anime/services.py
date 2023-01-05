from django.http import Http404

from .models import Anime, Review


def get_anime_by_slug(slug: str) -> Anime:
    try:
        return Anime.objects.get(slug=slug)
    except Anime.DoesNotExist:
        raise Http404


def create_review(data, user_id: int, anime_id: int) -> str:
    review = Review.objects.filter(user_id=user_id, anime_id=anime_id).first()
    if review:
        review.score = data.get('score', 0)
        review.save()
        return "Review was updated"

    data['user_id'] = user_id
    data['anime_id'] = anime_id
    review = Review(**data)
    review.save()
    return "Review was created"


def update_anime_score(value: int, anime: Anime) -> None:
    def get_anime_score(anime_id: int) -> float:
        reviews = Review.objects.filter(anime_id=anime_id, score__gt=0)
        if len(reviews) == 0:
            return 0

        score = 0
        for review in reviews:
            score += review.score
        return round(score / len(reviews), 2)

    if value == 0:
        return
    anime.score = get_anime_score(anime.pk)
    anime.save()
