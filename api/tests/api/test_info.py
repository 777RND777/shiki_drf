import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_user(client_with_user, user_payload):
    response = client_with_user.get(f'/{user_payload["username"]}/')
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert data['username'] == user_payload['username']
    assert 'password' not in data


@pytest.mark.django_db
def test_get_review_list(user_client, user_payload, animes_payload):
    completed_review = {'status': 'completed'}
    for anime in animes_payload:
        anime_slug = '-'.join(anime['title'].split(' '))
        _ = user_client.post(f'/animes/{anime_slug}/review', data=completed_review)

    response = user_client.get(f'/{user_payload["username"]}/list/anime')
    assert response.status_code == status.HTTP_200_OK
    data = response.data
    assert isinstance(data, list)
    assert len(data) == len(animes_payload)

    on_hold_review = {'status': 'on_hold', 'watched_episodes': 1}
    anime_slug = '-'.join(animes_payload[0]['title'].split(' '))
    _ = user_client.post(f'/animes/{anime_slug}/review', data=on_hold_review)

    response = user_client.get(f'/{user_payload["username"]}/list/anime/on_hold')
    assert response.status_code == status.HTTP_200_OK
    data = response.data
    assert isinstance(data, list)
    assert len(data) == 1
    response = user_client.get(f'/{user_payload["username"]}/list/anime/completed')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == len(animes_payload) - 1
