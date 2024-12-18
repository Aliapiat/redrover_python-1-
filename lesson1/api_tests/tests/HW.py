from http.client import responses
import pytest
import requests
from faker import Faker
from zope.component import handle

from lesson1.api_tests.case.pom.case import create_case
from lesson1.api_tests.case.models.case import Case
from lesson1.api_tests.case.data.case import create_case_dict, create_case_dict_high, create_case_error, check_id, \
    check_name
from lesson1.api_tests.utils.api_client import client


def test_create_case():
    response = create_case(Case(**create_case_dict).model_dump())
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(Case(**create_case_dict).model_dump())
    response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())


def test_create_case_high_priority():
    response = create_case(Case(**create_case_dict_high).model_dump())
    response.status_code_should_be_eq(200)
    response.json_should_be_eq(Case(**create_case_dict_high).model_dump())
    response.schema_should_be_eq(Case(**create_case_dict_high).model_json_schema())

def test_create_case_error422():
    response = client.make_request(
            handle="/testcases",
            method="POST",
            json={}
    )
    response.status_code_should_be_eq(422)



def test_check_id():
    response = create_case(Case(**check_id).model_dump())
    response.status_code_should_be_eq(200)
    response.value_with_key('id').should_be_eq(100)


def test_check_name():
    response = create_case(Case(**check_name).model_dump())
    response.status_code_should_be_eq(200)
    response.value_with_key('name').should_be_eq('Tim')



faker = Faker()

URL = 'http://127.0.0.1:8000/testcases/'
data = {
    "id": faker.random_number(3),
    "name": faker.text(8),
    "description": faker.sentence(6),
    "steps": [
        "string"
    ],
    "expected_result": "string",
    "priority": "низкий"
}
data2 = {
    "id": faker.random_number(4),
    "name": faker.text(8),
    "description": faker.sentence(6),
    "steps": [
        "string"
    ],
    "expected_result": "string",
    "priority": "высокий"
}
def create_tc():
    response = requests.post(URL, json=data)
    id = response.json()['id']
    return id

def test_create_tc():
    response = requests.get(URL+f'{create_tc()}')
    assert data['id'] == response.json()['id'] and data["name"] == response.json()["name"]

def test_get_tc():
    create_tc()
    response = requests.get(URL)
    assert response.status_code == 200

def test_get_tc_by_id():
    response = requests.get(URL+f'{create_tc()}')
    assert response.status_code == 200

def test_update_tc():
    response = requests.put(URL+f'{create_tc()}', json=data2)
    assert data2['id'] == response.json()['id'] and data2["name"] == response.json()["name"]

def test_delete_tc():
    response = requests.delete(URL + f'{create_tc()}')
    assert response.json()['detail'] == 'Test case deleted.'