from .models import User


def create_user(data: dict) -> User:
    user = User.objects.create_user(**data)
    return user
