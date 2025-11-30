import requests
import json


def all_posts():
    # response = requests.request('GET', 'http://objapi.course.qa-practice.com/object')
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    # print(json.dumps(response, indent=4, ensure_ascii=False))
    assert len(response["data"]) == 47, 'Not all posts returned'


def add_new_object():
    body = {"name": "Test Name",
            "data": {"test": "Lalala",
                     "desc": "Trula"}
            }
    headers = {'Content-Type': 'application/json'}
    response_post = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    # print(response_post)
    assert response_post.status_code == 200, 'Status code is incorrect'


def new_object():
    body = {"name": "Test Name",
            "data": {"test": "Lalala",
                     "desc": "Trula"}
            }
    headers = {'Content-Type': 'application/json'}
    response_post = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    # print(response_post)
    return response_post.json()['id']


def clear(pre_cond):
    response_delete = requests.delete(f'http://objapi.course.qa-practice.com/object/{pre_cond}')


def edit_all_object():
    pre_cond = new_object()
    body = {"name": "Test Name2",
            "data": {"test": "Update name",
                     "desc": "Trula"}
            }
    headers = {'Content-Type': 'application/json'}
    response_put = requests.put(
        f'http://objapi.course.qa-practice.com/object/{pre_cond}',
        json=body,
        headers=headers
    ).json()
    # print(response_put)
    assert response_put['name'] == 'Test Name2'
    clear(pre_cond)


def update_object():
    pre_cond = new_object()
    body = {"data": {"test": "random text - 0.1",
                     "desc": "Edit 2025"}
            }
    headers = {'Content-Type': 'application/json'}
    response_patch = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{pre_cond}',
        json=body,
        headers=headers
    ).json()
    print(response_patch)
    clear(pre_cond)


def delete_object():
    pre_cond = new_object()
    response_delete = requests.delete(f'http://objapi.course.qa-practice.com/object/{pre_cond}')
    print(response_delete)
    print(response_delete.status_code)


new_object()
