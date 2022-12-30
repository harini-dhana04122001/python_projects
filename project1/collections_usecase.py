import csv
import datetime
import logging
import os.path
import uuid

from CustomExceptions.invalid_exception import InvalidInputException
from constants import constant
from enum_classes.gender_enum import Gender
from project1 import booking_details
from project1.utilclass import validate_date, validate_number, validate_name, generate_id
from utilclass import calculate_age


details = dict()


class PassengerDetails:
    def __init__(self, passenger_uuid=None, passenger_name='', passenger_age=0, gender='', phone_number=None,
                 created_time=datetime.datetime.now()):
        self._passenger_uuid = passenger_uuid
        self._passenger_name = passenger_name
        self._passenger_age = passenger_age
        self._passenger_gender = gender.lower()
        self._phone_number = phone_number
        self._created_time: datetime = created_time

    def get_uuid(self):
        return self._passenger_uuid

    def set_uuid(self, passenger_uuid):
        self._passenger_uuid = passenger_uuid

    def get_name(self):
        return self._passenger_name

    def set_name(self, name):
        self._passenger_name = name

    def get_age(self):
        return self._passenger_age

    def set_age(self, date_of_birth):
        age = calculate_age(date_of_birth)
        self._passenger_age = age

    def get_gender(self):
        return self._passenger_gender

    def set_gender(self, gender):
        self._passenger_gender = gender.lower()

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_created_time(self):
        return self._created_time


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


passenger = PassengerDetails()
bookings = booking_details.BookingDetails()
count = 50


def generate_id():
    ids = uuid.uuid4()
    yield ids


def get_uuid_input():
    uuids = next(generate_id())
    passenger.set_uuid(uuids)


def get_booking_uuid_input():
    uuids = next(generate_id())
    bookings.set_booking_uuid(uuids)
    logging.info("UUID is successfully generated")


def get_name_input():
    name_ = input("Enter passenger name : ")
    valid_names = validate_name(name_)
    if not valid_names:
        logging.error("exception is raised for wrong input!")
        raise InvalidInputException("Not a valid name !")
    passenger.set_name(name_)
    logging.info("Name is added successfully after regex check")


def get_date_of_birth_input():
    date_of_birth_ = input("Enter passenger age : ")
    calculate_valid_age = validate_date(date_of_birth_)
    if not calculate_valid_age:
        logging.error("exception is raised for wrong input!")
        raise InvalidInputException("Not Valid Date of Birth !")
    passenger.set_age(date_of_birth_)
    logging.info("Age is successfully calculated")


def get_gender_input():
    gender_ = input("Enter passenger gender : ")
    if not gender_.lower() in [item.value for item in Gender]:
        logging.error("exception is raised for wrong input!")
        raise InvalidInputException("Not a valid gender !")
    passenger.set_gender(gender_)
    logging.info("Gender is added successfully")


def get_phone_number():
    phone_number_ = input("Enter contact number : ")
    valid_contact = validate_number(phone_number_)
    if not valid_contact:
        logging.error("exception is raised for wrong input!")
        raise InvalidInputException("Not valid contact number !")
    passenger.set_phone_number(phone_number_)
    logging.info("contact number is added successfully")


def get_seat_inputs():
    no_of_seats = int(input("Enter the number seats you want to book :\n"))
    global count
    count = count - no_of_seats
    if count > 0:
        print(f"{no_of_seats} booked out of {count} ")
        bookings.set_seats(no_of_seats)
    else:
        bookings.set_seats(None)
        logging.info("Seats cannot be added as seat cannot be added")
        return f'No seats available'


def add_passenger_details():

    no_inputs = int(input("enter no of passenger you need to add : "))
    for i in range(no_inputs):

        # # auto generating uuid and saving it.
        # get_uuid_input()
        #
        # # getting name from user,validating it and saving it
        # get_name_input()
        #
        # # getting date of birth from user,validating it and saving it
        # get_date_of_birth_input()
        #
        # # getting gender from user,validating it and saving it
        # get_gender_input()
        #
        # # getting phone number from user,validating it and saving it
        # get_phone_number()

        temp_dict = {'id': get_uuid_input(), 'name': get_name_input(), 'age': get_date_of_birth_input(),
                     'gender': get_gender_input(), 'contact_number': get_phone_number()}
        booking_details.setdefault(bookings.get_booking_uuid(), temp_dict)
        print(booking_details)
        # # storing entered data into csv file
        # with open(constant.PASSENGER_FILE_NAME, 'r+') as details:
        #     file_empty = os.stat(constant.PASSENGER_FILE_NAME).st_size == 0
        #     header = ["Passenger_id", "Name", "Age", "Gender", "PhoneNumber"]
        #     csv_write = csv.writer(details)
        #     if file_empty:
        #         csv_write.writerow(header)
        #         csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
        #                            passenger.get_gender(), passenger.get_phone_number()])
        #     else:
        #         csv_read = csv.reader(details)
        #         next(csv_read)
        #         csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
        #                            passenger.get_gender(), passenger.get_phone_number()])


def add_booking_details():
    no_inputs = int(input("enter no of passenger you need to add : "))
    for i in range(no_inputs):

        # auto generating uuid and saving it.
        get_booking_uuid_input()

        # getting name from user,validating it and saving it
        get_seat_inputs()

        # getting date of birth from user,validating it and saving it
        get_date_of_birth_input()

        # getting gender from user,validating it and saving it
        get_gender_input()

        # getting phone number from user,validating it and saving it
        get_phone_number()

        add_passenger_details()

        # storing entered data into csv file
        with open(constant.PASSENGER_FILE_NAME, 'r+') as details:
            file_empty = os.stat(constant.PASSENGER_FILE_NAME).st_size == 0
            header = ["Passenger_id", "Name", "Age", "Gender", "PhoneNumber"]
            csv_write = csv.writer(details)
            if file_empty:
                csv_write.writerow(header)
                csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
                                    passenger.get_gender(), passenger.get_phone_number()])
            else:
                csv_read = csv.reader(details)
                next(csv_read)
                csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
                                    passenger.get_gender(), passenger.get_phone_number()])


def main():
    is_working = True
    while is_working:
        print('Enter 1 to add passenger details\nEnter 2 to display passenger details')
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                add_booking_details()

            case '2':
                with open(constant.PASSENGER_FILE_NAME, 'r+') as details:
                    csv_read = csv.reader(details)
                    for i in csv_read:
                        print(i)

            case _:
                print("End of Service!")
                is_working = False


# if __name__ == "__main__":
#     flag = True
#     while flag:
#         try:
#             main()
#             flag = False
#         except Exception as ex:
#             print(f"\n--------- Exception handled : {ex} ----------")
