# import pytest
# class Test:
#
#     @pytest.mark.xfail(reason="Flaky test")
#     def test_get_token1(self,get_token):
#         token = get_token
#         print()
#         print(token)
#
#
#     def test_get_token2(self, get_token):
#         token = get_token
#         print()
#         print(token)
#
#
#     def test_get_token3(self, get_token):
#         token = get_token
#         print()
#         print(token)
#
# @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (4, 5, 9), (-4, 6, 2)])
# def test_check_sum(a, b, c):
#     assert a + b == c, f"Sum of {a} and {b} is not equal to {c}"

# def test(get_token):
#     token = get_token
#     print(token)
from data.generator.booking_generator import BookingGenerator
from functions import generate_checkin_checkout_dates

generator = BookingGenerator()


def test():
    checkin, checkout = generate_checkin_checkout_dates()
    info = next(generator.generate_bookings(checkin=checkin, checkout=checkout))
    print()
    print(info.first_name)
    print(info.last_name)
    print(info.total_price)
    print(info.deposit_paid)
    print(info.booking_dates)
    print(info.additional_needs)
    # data = generator.generate_bookings()
    # print(data)
    # print(data.last_name)