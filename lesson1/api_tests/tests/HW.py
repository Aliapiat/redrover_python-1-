from http.client import responses

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