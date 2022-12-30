"""
Creating descriptors using property decorators
"""


class Details:
    def __init__(self, age=17, name='harini'):
        self.age = age
        self.name = name

    @property
    def age_employee(self):
        return self.age

    @property
    def employee_name(self):
        return self.name

    @age_employee.setter
    def age_employee(self, age):
        self.age = age

    @employee_name.setter
    def employee_name(self, name):
        self.name = name

    @employee_name.deleter
    def employee_name(self):
        print('name instance deleted')
        del self.name

    @age_employee.deleter
    def age_employee(self):
        print('age instance deleted')
        del self.age


A1 = Details(21, "harini")
A2 = Details(22, "moni")
print(A1.age_employee)
print(f'hi {A2.employee_name}')
del A1.employee_name
del A2.age_employee
print(A2.employee_name)
#print(A2.age_employee)  # RAISE 'Details' object has no attribute 'age'
print("Age before giving new value : ", A1.age_employee)
A1.age_employee = 22
print("Age after giving new value : ", A1.age_employee)


# Creating descriptors using class methods
# """
#
#
# class Age:
#     def __init__(self, age=16, name='null'):
#         self.age = age
#         self.name = name
#
#     def __set__(self, obj, age):
#         if not 10 <= age <= 20:
#             raise ValueError('Valid age must be in [10, 20]')
#             self.age = age
#
#     def __set__(self, obj, name):
#         self.name = name
#
#     def __get__(self, obj, type=int):
#         return self.age
#
#     def __get__(self, obj, type=str):
#         return self.name
#
#
# class Student:
#     age = Age()
#
#     def __init__(self, name, age, std):
#         self.std = std
#         self.name = name
#         self.age = age
#
#         print(f'Student Name: {self.name}, Age:{self.age}, Class:{self.std}')
#
#     def __set__(self, obj, std):
#         self.std = std
#
#     def __get__(self, obj, type=str):
#         return self.std


# S1 = Student("John", 17, '12B')
# S2 = Student("Mike", 19, '12A')
