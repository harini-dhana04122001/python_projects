""" INHERITANCE """


# parent class
class Bird:

    def __init__(self, color):
        self.color = color
        print(f"{self.color} Bird is ready")

    def who_is_this(self):
        print("Bird")

    @staticmethod
    def swim():
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self, new, color):
        Bird.__init__(self, color)
        self.new = new
        print(f"{self.new} {self.color} Penguin is ready")

    # def __init__(self, color, new):
    #     # call super() function
    #     super().__init__(color)    # super() is always preferable
    #     self.new = new
    #     print(f"{self.new} {self.color} Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin(1, "red")
parrot = Bird("red")
parrot.who_is_this()
peggy.who_is_this()
peggy.swim()
peggy.run()


class PayrollSystem:

    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Credited amount: {employee.calculate_payroll()}')
            print('')


# Parent Class
class Employee:
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name


# child class for parent employee
class SalaryEmployee(Employee):
    def __init__(self, id, name, gross_salary):
        super().__init__(id, name)
        self.gross_salary = gross_salary

    def calculate_payroll(self):
        return self.gross_salary


# hierarchical inheritance
# Child class for parent SalaryEmployee
class SalaryAllowance(SalaryEmployee):
    def __init__(self, id, name, gross_salary, medical_insurance):
        super().__init__(id, name, gross_salary)
        self.medical_insurance = medical_insurance

    def calculate_payroll(self):
        pay = super().calculate_payroll()
        return pay - self.medical_insurance


# hierarchical inheritance
# Child class for parent SalaryEmployee
class EmployeePf(SalaryEmployee):
    def __init__(self, id, name, gross_salary, pf_percentage):
        super().__init__(id, name, gross_salary)
        self.pf_percentage = pf_percentage

    def calculate_payroll(self):
        pay = super().calculate_payroll()
        return pay/self.pf_percentage


# Multilevel inheritance
# Child class for SalaryAllowance
class FinalPayCalculation(SalaryAllowance):
    def __init__(self, id, name, gross_salary, medical_insurance, tax_percentage, pf_percentage):
        super().__init__(id, name, gross_salary, medical_insurance)
        self.tax_percentage = tax_percentage

    def calculate_payroll(self):
        new_pay = super().calculate_payroll()
        tax = (new_pay/self.tax_percentage)-200
        return round((new_pay - tax)/12, 2)


pf = EmployeePf(1,'harini',300000, 50)
pay_calculation = FinalPayCalculation(1, 'Harini', 300000, 4500, 10, pf_percentage=2)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll([pay_calculation, pf])
