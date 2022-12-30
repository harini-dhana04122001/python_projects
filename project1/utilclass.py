import re
import uuid
from datetime import datetime


def validate_number(number):
    valid_number = re.match(
        '^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$', number)
    if not valid_number:
        return False
    else:
        return True


def validate_date(date):
    valid_date = re.match('^[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}$', date)
    return valid_date


def validate_name(name):
    valid_name = re.match('[a-zA-Z]{1,30}', name)
    return valid_name


def calculate_age(date_of_birth):
    today_date = datetime.today()
    age = today_date.year - int(date_of_birth[6:10]) - (
            (today_date.month, today_date.day) < (int(date_of_birth[3:5]), int(date_of_birth[0:2])))
    return age


def generate_id():
    ids = uuid.uuid4()
    yield ids
