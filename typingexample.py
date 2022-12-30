from typing import Dict
from typing import List
from typing import NewType


def greeting(names: List[str]) -> str:
    return 'Hello, {}'.format(', '.join(names))


# greeting([1, 2, 3])  # Expected type 'list[str]', got 'list[int]' instead
greeting(['harini', 'dhivya', 'sivadharshini'])

# Create a new user type called 'temperature_change'
temperature_change = NewType('StudentID', List[int])


def get_student_name(temp_changes: temperature_change) -> str:
    return str(input(f'Enter username for ID [{temp_changes}]:\n'))


stud_a = get_student_name(temperature_change([32, 24, 30]))
print(stud_a)

'''This is incorrect!!'''
# stud_a = get_student_name(temperature_change(['32', '24', '30']))
# print(stud_a)

'''This is incorrect!!'''


# stud_b = get_student_name(-1)
# print(stud_b)


def student_details(details: Dict[str, str | int]) -> str:
    keys = details.keys()
    return 'Hello, {}'.format(', '.join(keys))


student_details({'name': 'vidhya', 'age': 17, 'class': '12B'})
''' incorrect one '''


# student_details({1: 'hi', 2: 'welcome'})  # Expected type 'dict[str, str | int]', got 'dict[int, str]' instead


def check_if_greater(value: int) -> bool:
    if value > 10:
        return True
    else:
        return False


check_if_greater(12)
# check_if_greater(zip({1, 2, 3}, {2, 3, 4}))    # Expected type 'int', got 'zip[tuple[int, int]]' instead
