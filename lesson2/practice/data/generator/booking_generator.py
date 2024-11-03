from data.generator.base_generator import BaseGenerator
from data.dataclasses.booking_data import BookingData, BookingDates

class BookingGenerator(BaseGenerator):


    def generate_booking_dates(self, booking_dates, checkin, checkout):
        if booking_dates is None:
            return BookingDates(checkin=checkin, checkout=checkout)
        return booking_dates


    def generate_bookings(self, first_name=None, last_name=None, total_price=None, deposit_paid=True,
                 booking_dates=None, additional_needs=None, checkin=None, checkout=None):
        yield BookingData(
            first_name=self.get_first_name(first_name),
            last_name=self.get_last_name(last_name),
            total_price=self.get_random_number(total_price),
            deposit_paid=deposit_paid,
            booking_dates=self.generate_booking_dates(booking_dates, checkin, checkout),
            additional_needs=self.get_random_word(additional_needs)
        )