from pytest_voluptuous import S

from schemas import users_list, single_user, user1
from utils.sessions import reqres


def test_list_users():
    response = reqres().get('/users', params={'page': 8, 'per_page': 1})

    assert response.status_code == 200
    assert S(users_list) == response.json()


def test_single_user_by_id():
    response = reqres().get('/users', params={'id': 8})

    assert response.status_code == 200
    assert S(single_user) == response.json()


def test_registration_unsuccess():
    response = reqres().post('/register', params={"email": "sydney@fife"})

    assert response.status_code == 400


def test_create_user():
    response = reqres().post('/users', params={'name': 'Eugeny', 'job': 'smetchik'})

    assert response.status_code == 201


def test_delete_user():
    response = reqres().delete('/users', params={'id': 14})

    assert response.status_code == 204

