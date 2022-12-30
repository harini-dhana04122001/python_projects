import logging

from enum_classes.booking_status import BookingStatus
from project1.utilclass import generate_id

count = 50


def get_booking_uuid_input(booking_obj):
    uuids = next(generate_id())
    booking_obj.set_booking_uuid(uuids)
    logging.info("UUID is successfully generated")


def get_seat_inputs(booking_obj):
    no_of_seats = int(input("Enter the number seats you want to book :\n"))
    global count
    count = count - no_of_seats
    if count > 0:
        print(f"{no_of_seats} booked out of {count} ")
        booking_obj.set_seats(no_of_seats)
    else:
        booking_obj.set_seats(None)
        logging.info("Seats cannot be added as seat cannot be added")
        return f'No seats available'


def get_booking_status(booking_obj):
    if booking_obj.get_seats() is None:
        booking_obj.set_booking_status(BookingStatus('2').name)
        logging.info("booking status is Booking Failed")
    else:
        booking_obj.set_booking_status(BookingStatus('1').name)
        logging.info("booking status is Booking Successful")


def add_booking_details(booking_obj, inputs):
    for i in range(inputs):
        # auto generating uuid and saving it.
        get_booking_uuid_input(booking_obj)

        # getting name from user,validating it and saving it
        get_seat_inputs(booking_obj)

        # getting booking status from user,validating it and saving it
        get_booking_status(booking_obj)
