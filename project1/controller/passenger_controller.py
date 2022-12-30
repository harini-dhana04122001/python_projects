import csv
import logging
import os
from CustomExceptions.invalid_exception import InvalidInputException
from constants.constant import PASSENGER_FILE_NAME
from enum_classes.gender_enum import Gender
from project1.booking_details import BookingDetails
from project1.controller.booking_controller import add_booking_details
from project1.passenger_details import PassengerDetails
from project1.utilclass import validate_date, validate_number, validate_name, generate_id

passenger = PassengerDetails()
bookings_obj = BookingDetails()
bookings_detail = dict()


def get_uuid_input():
    uuids = next(generate_id())
    passenger.set_uuid(uuids)


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
    else:
        with open(PASSENGER_FILE_NAME, 'r+') as details_:
            csv_reader = csv.reader(details_)
            for row1 in csv_reader:
                if not row1:
                    continue
                elif row1[4] != phone_number_:
                    raise InvalidInputException("contact number already exist")
                else:
                    passenger.set_phone_number(phone_number_)
                    logging.info("contact number is added successfully")
                    return f'Successfully registered contact number'


def add_passenger_details():

    no_inputs = int(input("enter no of passenger you need to add : "))
    for i in range(no_inputs):

        # auto generating uuid and saving it.
        get_uuid_input()

        # getting name from user,validating it and saving it
        get_name_input()

        # getting date of birth from user,validating it and saving it
        get_date_of_birth_input()

        # getting gender from user,validating it and saving it
        get_gender_input()

        # getting phone number from user,validating it and saving it
        get_phone_number()

        add_booking_details(bookings_obj, no_inputs)

        temp_dict = {'id': passenger.get_uuid(), 'name': passenger.get_name(), 'age': passenger.get_age(),
                     'gender': passenger.get_age(), 'contact_number': passenger.get_phone_number()}
        # booking_details_.setdefault(bookings.get_booking_uuid(), temp_dict)
        # print(booking_details_)
        print(temp_dict)
        bookings_detail.setdefault(bookings_obj.get_booking_uuid(), temp_dict)
        print(bookings_detail)

        # storing entered data into csv file
        with open(PASSENGER_FILE_NAME, 'r+') as details:
            file_empty = os.stat(PASSENGER_FILE_NAME).st_size == 0
            header = ["Passenger_id", "Name", "Age", "Gender", "PhoneNumber", "BookingId", "NoOfSeatsBooked",
                      "BookingStatus"]
            csv_write = csv.writer(details)
            if file_empty:
                csv_write.writerow(header)
                csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
                                    passenger.get_gender(), passenger.get_phone_number(),
                                    bookings_obj.get_booking_uuid(), bookings_obj.get_seats(),
                                    bookings_obj.get_booking_status()])
            else:
                csv_read = csv.reader(details)
                next(csv_read)
                csv_write.writerow([passenger.get_uuid(), passenger.get_name(), passenger.get_age(),
                                    passenger.get_gender(), passenger.get_phone_number(),
                                    bookings_obj.get_booking_uuid(), bookings_obj.get_seats(),
                                    bookings_obj.get_booking_status()])


def display_details_by_id():
    id_input = input("enter unique id of passenger : ")
    with open(PASSENGER_FILE_NAME, 'r') as details:
        for row in details.readlines():
            data = row.replace('\n', '').split(',')
            if data[0] == id_input:
                print(list([data[0], data[1], data[2], data[3], data[3], data[4], data[5], data[6], data[7]]))


def display_details_by_contact_number():
    contact_number = input("enter unique id of passenger : ")
    with open(PASSENGER_FILE_NAME, 'r+') as details_:
        csv_reader = csv.reader(details_)
        for row1 in csv_reader:
            if not row1:
                continue
            elif row1[4] == contact_number:
                print(row1)
