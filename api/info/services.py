from django.db.models import QuerySet
from django.shortcuts import get_object_or_404

from anime.models import Review
from users.models import User


def get_user_reviews(slug: str, status: str) -> QuerySet[Review]:
    user_id = get_object_or_404(User, slug=slug).pk
    if len(status) == 0:
        return Review.objects.filter(user_id=user_id).select_related()
    return Review.objects.filter(user_id=user_id, status=status).select_related()
