import requests
from pprint import pprint
from http import HTTPStatus
from lesson2.practice.src.assertions import assertions

URL = "https://restful-booker.herokuapp.com/booking"

def test_get_token():
    response = requests.get(URL)
    assertions.assert_status_code(response, HTTPStatus.OK)
    lst = [i["bookingid"] for i in response.json()]
    pprint(lst)