import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_user(client_with_user, user_payload):
    response = client_with_user.get(f'/{user_payload["username"]}/')
    assert response.status_code == status.HTTP_200_OK

    data = response.data
    assert data['username'] == user_payload['username']
    assert 'password' not in data
