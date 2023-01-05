from django.http import Http404

from users.models import User


def get_user_by_slug(slug):
    try:
        return User.objects.get(slug=slug)
    except User.DoesNotExist:
        raise Http404
