from celery.app import shared_task

from .models import Anime, Review


@shared_task()
def update_anime_score(id_: int) -> None:
    def get_anime_score(anime_id: int) -> float:
        reviews = Review.objects.filter(anime_id=anime_id, score__gt=0)
        if len(reviews) == 0:
            return 0

        score = 0
        for review in reviews:
            score += review.score
        return round(score / len(reviews), 2)

    anime = Anime.objects.get(id=id_)
    anime.score = get_anime_score(id_)
    anime.save()
