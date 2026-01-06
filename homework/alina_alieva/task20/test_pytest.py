import requests
import pytest


@pytest.fixture()
def pre_condition_new_object_id():
    body = {"name": "Object Test", "data": {"test": "Body data 1", "desc": "Data 2"}}
    headers = {'Content-Type': 'application/json'}
    response_obj = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response_obj.json()['id']
    print(object_id)
    yield object_id
    print('deleting the object...')
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session', autouse=True)
def text_title():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function', autouse=True)
def text_after_each_test():
    print('before test')
    yield
    print('after test')


@pytest.mark.critical
def test_get_one_object(pre_condition_new_object_id, text_title):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{pre_condition_new_object_id}').json()
    assert response["id"] == pre_condition_new_object_id


@pytest.mark.critical
@pytest.mark.parametrize(
    "body",
    [
        {"name": "Object Test one", "data": {"test": "Body data 1", "desc": "Data 1"}},
        {"name": "Object Test two", "data": {"test": "Body data 2", "desc": "Data 2"}},
        {"name": "Object Test three", "data": {"test": "Body data 3", "desc": "Data 3"}}

    ]
)
def test_add_new_object(body):
    headers = {'Content-Type': 'application/json'}
    response_post = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response_post.status_code == 200, 'Status code is incorrect'
    object_id = response_post.json()['id']
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.mark.medium
# @pytest.mark.skip('No preconditions')
def test_edit_all_object():
    body_create = {"name": "Object for edit", "data": {"test": "Test", "desc": "Desc"}}
    headers = {'Content-Type': 'application/json'}
    response_create = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body_create,
        headers=headers
    )
    object_id = response_create.json()['id']

    body = {"name": "Test Name2", "data": {"test": "Update name", "desc": "Trula"}}
    headers = {'Content-Type': 'application/json'}
    response_put = requests.put(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response_put['name'] == 'Test Name2'
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


# @pytest.mark.skip('No preconditions')
def test_update_object():
    body_create = {"name": "Object for patch", "data": {"test": "Test", "desc": "Desc"}}
    headers = {'Content-Type': 'application/json'}
    response_create = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body_create,
        headers=headers
    )
    object_id = response_create.json()['id']

    body = {"data": {"test": "random text - 0.1", "desc": "Edit 2025"}}
    headers = {'Content-Type': 'application/json'}
    response_patch = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response_patch['data']['test'] == "random text - 0.1"
    requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')


# @pytest.mark.skip('No preconditions')
def test_delete_object():
    body_create = {"name": "Object for delete", "data": {"test": "Test", "desc": "Desc"}}
    headers = {'Content-Type': 'application/json'}
    response_create = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body_create,
        headers=headers
    )
    object_id = response_create.json()['id']
    response_delete = requests.delete(f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response_delete.status_code == 200
