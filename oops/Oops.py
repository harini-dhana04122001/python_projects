""" CLASS, OBJECT AND METHOD """


# This is for class implementation where an object is instantiated
class Shapes:

    # class attribute
    dimension = "2-D"

    # instance attribute
    def __init__(self, shape_name, sides):
        self.shape_name = shape_name
        self.sides = sides


# instantiate the  class
shape_1 = Shapes("square", 4)
shape_2 = Shapes("circle", 0)

# access the class attributes
print("shape_1 is a {} shape".format(Shapes.dimension))
print("shape_1 is also a {} shape".format(shape_1.__class__.dimension))
Shapes.dimension = "3-D"
print("shape_2 is also a {} shape".format(shape_2.__class__.dimension))

# access the instance attributes
print("{} has {} sides".format(shape_1.shape_name, shape_1.sides))
print(f'{shape_1.shape_name} has {shape_1.sides} sides')
print("{} has {} sides".format(shape_2.shape_name, shape_2.sides))


# This is an example for class with different methods
class Employee:
    office_name = None   # Class attribute

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def company_name(cls, office_name="ideas2it"):
        cls.office_name = office_name
        return office_name

    @staticmethod
    def annual_salary(salary):
        monthly_salary = (salary/12)-(salary/50)
        return monthly_salary

    def get_employee_details(self, salary=None):
        return self.name, self.age, self.office_name, self.annual_salary(salary)


# emp1 = Employee()
emp2 = Employee("harini",21)
emp2.company_name("zoho")
print(emp2.get_employee_details(300000))


# CONSTRUCTOR
class Details:
    def __init__(self,name=None,age=None,phone_number=None):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def employee_name(self, name):
        self.name = name

    def employee_age(self, age):
        return age

    def contact_number(self, phone_number):
        return phone_number

    def employee_name(self,name):
        self.name = name

    def employee_age(self,age):
        self.age = age

    def contact_number(self,phone_number):
        self.phone_number = phone_number
