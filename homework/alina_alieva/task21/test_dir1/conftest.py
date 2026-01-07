import pytest
import requests


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


@pytest.fixture()
def pre_cond_new_object_id_without_del():
    body = {"name": "Object Test", "data": {"test": "Body data 1", "desc": "Data 2"}}
    headers = {'Content-Type': 'application/json'}
    response_obj = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    object_id = response_obj.json()['id']
    print(object_id)
    return object_id


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
