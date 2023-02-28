import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_anime_list(client_with_anime, n):
    response = client_with_anime.get(f'/animes/')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == n

    response = client_with_anime.get(f'/animes/kind/movie')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1

    response = client_with_anime.get(f'/animes/status/released')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1

    response = client_with_anime.get(f'/animes/genre/genre-1')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == n - 1

    response = client_with_anime.get(f'/animes/studio/studio-1')
    assert response.status_code == status.HTTP_200_OK
    data = response.data['results']
    assert isinstance(data, list)
    assert len(data) == 1
