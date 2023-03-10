from .models import Anime, Review


def get_anime_list(config: dict) -> Anime:
    filter_kwargs = {}
    if 'kind' in config:
        filter_kwargs['kind'] = config['kind']
    if 'status' in config:
        filter_kwargs['status'] = config['status']
    if 'genre' in config:
        filter_kwargs['genres__slug'] = config['genre']
    if 'studio' in config:
        filter_kwargs['studio__slug'] = config['studio']
    return Anime.objects.filter(**filter_kwargs)


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
