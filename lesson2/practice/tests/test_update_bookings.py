import requests
from lesson2.practice.data.urls import urls
from http import HTTPStatus

from src.assertions import assertions


def test_update_booking(get_token, create_booking):
    data2 = {
        "firstname" : "James",
        "lastname" : "Brown"
    }
    book_id = create_booking["bookingid"]
    requests.patch(f"{urls.URL}/{book_id}", json=data2, headers={"Cookie": f"token={get_token}"})
    response = requests.get(f"{urls.URL}/{book_id}")
    firstname = response.json()["firstname"]
    lastname = response.json()["lastname"]
    assertions.assert_last_first_name([firstname, lastname], ["James", "Brown"])

#
# def test_update_booking1():
#     data = {
#         "firstname" : "David",
#         "lastname" : "Davidov",
#         "totalprice" : 55,
#         "depositpaid" : True,
#         "bookingdates" : {
#             "checkin" : "2018-01-01",
#             "checkout" : "2019-01-01"
#         },
#     "additionalneeds" : "Breakfast"
#     }
#
#     data1 = {
#         "username" : "admin",
#         "password" : "password123"
#     }
#
#     data2 = {
#         "firstname" : "James",
#         "lastname" : "Brown"
#     }
#
#     response1 = requests.post(URL, json=data)
#     book_id = response1.json()["bookingid"]
#
#     response2 = requests.post(URL_AUTH, json=data1)
#     token = response2.json()["token"]
#
#     requests.patch(f"{URL}/{book_id}", json=data2, headers={"Cookie": f"token={token}"})
#
#     response3 = requests.get(f"{URL}/{book_id}")
#
#     firstname = response3.json()["firstname"]
#     lastname = response3.json()["lastname"]
#
#     assert firstname == "James"
#     assert lastname == "Brown"
