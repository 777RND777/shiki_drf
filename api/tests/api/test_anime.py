import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_anime_list(client_with_anime, n):
    response = client_with_anime.get('/animes/')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == n

    response = client_with_anime.get('/animes/kind/movie')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1

    response = client_with_anime.get('/animes/status/released')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1

    response = client_with_anime.get('/animes/genre/genre-1')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == n - 1

    response = client_with_anime.get('/animes/studio/studio-1')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1


@pytest.mark.django_db
def test_get_anime_detail(client_with_anime, animes_payload):
    anime_slug = '-'.join(animes_payload[0]['title'].split(' '))
    response = client_with_anime.get(f'/animes/fake-{anime_slug}')
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = client_with_anime.get(f'/animes/{anime_slug}')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_review_anime(user_client, animes_payload):
    wrong_review = {'status': 'watched'}
    planned_review = {'status': 'planned'}
    on_hold_review = {'score': 1, 'status': 'on_hold', 'watched_episodes': 1}
    completed_review = {'score': 10, 'status': 'completed'}

    anime_slug = '-'.join(animes_payload[0]['title'].split(' '))
    response = user_client.post(f'/animes/fake-{anime_slug}/review', data=planned_review)
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = user_client.post(f'/animes/{anime_slug}/review', data=wrong_review)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = user_client.post(f'/animes/{anime_slug}/review', data=planned_review)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['watched_episodes'] == 0

    response = user_client.post(f'/animes/{anime_slug}/review', data=on_hold_review)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['watched_episodes'] == on_hold_review['watched_episodes']

    response = user_client.post(f'/animes/{anime_slug}/review', data=completed_review)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['watched_episodes'] == animes_payload[0]['episodes']
