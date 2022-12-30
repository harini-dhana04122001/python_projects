class Calculator:

    def __init__(self,number1,number2,number3):
        self.first_number = number1
        self.second_number = number2
        self.third_number = number3

    def add(self):
        print(f"addition of two numbers is {self.first_number + self.second_number + self.third_number}")


class EmployeeDetails:

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def add(self):
        print(f'employee name: {self.name}\nemployee id : {self.employee_id}')


def testing_polymorphism(tests):
    tests.add()


# instantiate objects
blu = Calculator(2, 4, 6)
peggy = EmployeeDetails('harini', 12)
# passing the object
testing_polymorphism(blu)
testing_polymorphism(peggy)