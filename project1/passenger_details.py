import datetime

from project1.utilclass import calculate_age


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
