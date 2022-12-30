import datetime


class BookingDetails:
    def __init__(self, booking_uuid=None, no_of_seats='', price=500, booking_status='', is_active=True,
                 created_time=datetime.datetime.now()):
        self._booking_uuid = booking_uuid
        self._no_of_seats = no_of_seats
        self._price = price
        self._booking_status = booking_status.lower()
        self._active_status = is_active
        self._created_time: datetime = created_time

    def get_booking_uuid(self):
        return self._booking_uuid

    def set_booking_uuid(self, booking_uuid):
        self._booking_uuid = booking_uuid

    def get_seats(self):
        return self._no_of_seats

    def set_seats(self, seats):
        self._no_of_seats = seats

    def get_price(self):
        return self._price

    def set_price(self, price):
        total_price = price * self.get_seats()
        self._price = total_price

    def get_booking_status(self):
        return self._booking_status

    def set_booking_status(self, booking_status):
        self._booking_status = booking_status.lower()

    def get_active_status(self):
        return self._active_status

    def set_active_status(self, active_status):
        self._active_status = active_status

    def get_created_time(self):
        return self._created_time
