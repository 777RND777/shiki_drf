from django.db.models import QuerySet
from django.http import Http404

from anime.models import Review
from users.models import User


def get_user_by_slug(slug: str) -> User:
    try:
        return User.objects.get(slug=slug)
    except User.DoesNotExist:
        raise Http404


def get_user_reviews(slug: str, status: str) -> QuerySet[Review]:
    user_id = get_user_by_slug(slug).pk
    if len(status) == 0:
        return Review.objects.filter(user_id=user_id).select_related()
    return Review.objects.filter(user_id=user_id, status=status).select_related()
