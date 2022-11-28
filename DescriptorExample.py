"""
Creating descriptors using property decorators
"""


class Age:
    def __init__(self, age=17, name='harini'):
        self.age = age
        self.name = name

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, _age):
        if not 10 <= _age <= 20:
            raise ValueError('Valid age must be in [10, 20]')
            self._age = _age

    @name.setter
    def name(self, _name):
        self._name = _name


class Student:
    age = Age()

    def __init__(self, name, age, std):
        self.std = std
        self.name = name
        self.age = age

        print(f'Student Name: {self.name}, Age:{self.age}, Class:{self.std}')

    @property
    def standard(self):
        return self.std

    @standard.setter
    def __set__(self, obj, std):
        self.std = std


S1 = Student("John", 17, '12B')
S2 = Student("Mike", 19, '12A')


# """
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
#
#
# S1 = Student("John", 17, '12B')
# S2 = Student("Mike", 19, '12A')
