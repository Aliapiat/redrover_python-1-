import pytest
import requests
from data.urls import Urls
import os
from dotenv import load_dotenv

load_dotenv()

urls = Urls()
# @pytest.fixture()
# def get_token():
#     print()
#     print("Get token")
#     return "Token 12325325"

admin = os.environ.get("USERNAME_ADMIN")
password = os.environ.get("PASSWORD_ADMIN")

@pytest.fixture(scope="session")
def get_token():
    data1 = {
        "username" : admin,
        "password" : password
    }

    response2 = requests.post(urls.URL_AUTH, json=data1)
    token = response2.json()["token"]
    return token


@pytest.fixture
def create_booking():
    data = {
            "firstname" : "David",
            "lastname" : "Davidov",
            "totalprice" : 55,
            "depositpaid" : True,
            "bookingdates" : {
                "checkin" : "2018-01-01",
                "checkout" : "2019-01-01"
            },
        "additionalneeds" : "Breakfast"
        }
    response = requests.post(urls.URL, json=data)
    booking = response.json()
    return booking