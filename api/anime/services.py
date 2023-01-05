from django.http import Http404

from .models import Anime, Review


def get_anime_by_slug(slug: str) -> Anime:
    try:
        return Anime.objects.get(slug=slug)
    except Anime.DoesNotExist:
        raise Http404


def create_review(data: dict, user_id: int, anime_id: int) -> Review:
    review = Review.objects.filter(user_id=user_id, anime_id=anime_id).select_related().first()
    if review:
        return update_review(review, data)

    review = Review(user_id=user_id, anime_id=anime_id, **data)
    if review.status == Review.Status.COMPLETED:
        review.watched_episodes = review.anime.episodes
    review.save()
    return review


def update_review(review: Review, data: dict) -> Review:
    review.watched_episodes = data.get('watched_episodes', review.watched_episodes)
    if data.get('status') == Review.Status.COMPLETED and review.status != data.get('status'):
        review.watched_episodes = review.anime.episodes
    review.status = data.get('status', review.status)
    review.score = data.get('score', review.score)
    review.text = data.get('text', review.text)
    review.save()
    return review


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