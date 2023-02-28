import pytest
from rest_framework.test import APIClient

from anime.models import Anime, Genre, Studio
from users.models import User


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def n():
    return 3


@pytest.fixture
def genres_payload(n):
    return [{'name': f'genre {x}'} for x in range(n)]


@pytest.fixture
def studios_payload(n):
    return [{'name': f'studio {x}'} for x in range(n)]


@pytest.fixture
def animes_payload():
    return [
        {
            'title': 'title 1',
            'kind': 'tv',
            'episodes': 13,
            'status': 'ongoing',
        },
        {
            'title': 'title 2',
            'kind': 'movie',
            'episodes': 1,
            'status': 'anons',
        },
        {
            'title': 'title 3',
            'kind': 'tv',
            'episodes': 150,
            'status': 'released',
        },
    ]


@pytest.fixture
def user_payload():
    return {
        'username': 'test_username',
        'password': 'test_password',
    }


@pytest.fixture
def user_change_payload():
    return {
        'username': 'new_username',
        'password': 'new_password'
    }


@pytest.fixture
def filled_client(client, n, genres_payload, studios_payload, animes_payload):
    genres = [Genre.objects.create(**genre) for genre in genres_payload]
    studios = [Studio.objects.create(**studio) for studio in studios_payload]
    for i, anime in enumerate(animes_payload):
        studio = studios[min(i, n - 1)]
        anime = Anime(studio=studio, **anime)
        anime.save()
        anime.genres.add(*genres[i:n])
        anime.save()
    return client


@pytest.fixture
def user_client(client, user_payload):
    _ = client.post('/users/sign_up', user_payload)
    token = client.post('/users/sign_in', user_payload).data['token']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
