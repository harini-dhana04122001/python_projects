from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def details(self):
        pass


class Car(AbstractClass):
    def __init__(self, model, price, release_year):
        self.model = model
        self.price = price
        self.release_year = release_year

    def details(self):
        return f'model of the car is : {self.model}\nprice of this model is : {self.price}\n' \
               f'release_year of this model : {self.release_year}'


class Employee(AbstractClass):
    def __init__(self, name, role, dob):
        self.name = name
        self.role = role
        self.dob = dob

    def details(self):
        return f'name of the employee is : {self.name}\nrole : {self.role}\n' \
               f'date of birth : {self.dob}'


obj1 = Car("Toyota", 1000000, '20-11-2022')
print(obj1.details())

obj2 = Employee("Harini", "Trainee", "04-12-2001")
print(obj2.details())

print(isinstance(obj1, AbstractClass))
