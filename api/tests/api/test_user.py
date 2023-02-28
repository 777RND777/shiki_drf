import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_user_list(client_with_user):
    response = client_with_user.get('/users/')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) > 0


@pytest.mark.django_db
def test_sign_up(client, user_payload):
    response = client.post('/users/sign_up', {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client.post('/users/sign_up', {'username': user_payload['username']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client.post('/users/sign_up', {'password': user_payload['password']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client.post('/users/sign_up', {'username': user_payload['username'], 'password': ''})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client.post('/users/sign_up', {'username': '', 'password': user_payload['password']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.post('/users/sign_up', user_payload)
    assert response.status_code == status.HTTP_201_CREATED

    data = response.data
    assert data['username'] == user_payload['username']
    assert 'password' not in data

    response = client.post('/users/sign_up', user_payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_sign_in(client_with_user, user_payload):
    response = client_with_user.post('/users/sign_in', {'username': user_payload['username']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client_with_user.post('/users/sign_in', {'password': user_payload['password']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    response = client_with_user.post('/users/sign_in',
                                     {'username': 'incorrect_username', 'password': user_payload['password']})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client_with_user.post('/users/sign_in', user_payload)
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data
