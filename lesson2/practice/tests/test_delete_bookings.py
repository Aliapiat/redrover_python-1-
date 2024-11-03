from http import HTTPStatus

import requests
from lesson2.practice.data.urls import urls

def test_delete_booking(get_token, create_booking):
    book_id = create_booking["bookingid"]
    requests.delete(f"{urls.URL}/{book_id}", headers={"Cookie": f"token={get_token}"})
    response3 = requests.get(f"{urls.URL}/{book_id}", headers={"Cookie": f"token={get_token}"})
    assert response3.status_code == HTTPStatus.NOT_FOUND


# def test_delete_booking1():
#
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
#     response1 = requests.post(URL, json=data)
#     book_id = response1.json()["bookingid"]
#
#     response2 = requests.post(URL_AUTH, json=data1)
#     token = response2.json()["token"]
#
#     requests.delete(f"{URL}/{book_id}", headers={"Cookie": f"token={token}"})
#
#     response3 = requests.get(f"{URL}/{book_id}", headers={"Cookie": f"token={token}"})
#     assert response3.status_code == 404