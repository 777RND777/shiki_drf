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
    anime_slug = "-".join(animes_payload[0]['title'].split(" "))
    response = client_with_anime.get(f'/animes/fake-{anime_slug}')
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = client_with_anime.get(f'/animes/{anime_slug}')
    assert response.status_code == status.HTTP_200_OK
