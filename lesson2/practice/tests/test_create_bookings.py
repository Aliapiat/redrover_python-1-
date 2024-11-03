from http import HTTPStatus
from pprint import pprint
from lesson2.practice.data.urls import urls
import requests
from lesson2.practice.src.assertions import assertions
from lesson2.practice.src.modules.create_booking_module import CreateBookingModule
from lesson2.practice.data.generator.booking_generator import BookingGenerator
from lesson2.practice.functions import generate_checkin_checkout_dates

generator = BookingGenerator()

URL = "https://restful-booker.herokuapp.com/booking"

module = CreateBookingModule()

def test_create_booking():
    data = {
        "firstname": "Denis",
        "lastname": "Denisov",
        "totalprice": 55,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response1 = requests.post(URL, json=data)
    firstname = response1.json()["booking"]["firstname"]
    lastname = response1.json()["booking"]["lastname"]
    booking_id = response1.json()["bookingid"]

    assertions.assert_status_code(response1, HTTPStatus.OK)

    response2 =requests.get(f"{URL}/{booking_id}")
    firstname1 = response2.json()["firstname"]
    lastname1 = response2.json()["lastname"]

    assertions.assert_status_code(response2, HTTPStatus.OK)
    assertions.assert_last_first_name([firstname, lastname], [firstname1, lastname1])

def test_create_booking2():
    checkin, checkout = generate_checkin_checkout_dates()
    info = next(generator.generate_bookings(checkin=checkin, checkout=checkout))
    data = module.create_data(info=info)
    response = requests.post(urls.URL, json=data)
    print(response.json())
