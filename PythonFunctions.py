"""def show_details(name, age=20):
    print("name of the employee is ", name, "and their age is ", age, "\n")


show_details('Harini')
show_details('Saira Begum', 21)    # output of age will be 21 as argument for age is given
"""


def show_details(name, *args):
    print("name of the employee is ", name, "and their hobby is ", *args, "\n")


show_details('Harini')
# output of age will be 21 as argument for age is given
show_details('Saira Begum', 'listening to music','drawing','watching anime')


# Positional and Keyword argument examples
def deposit_calculator(deposit_amount, actual_balance):
    new_balance = actual_balance + deposit_amount
    print("current balance is ", new_balance, "\n")


# # Here the keyword for both arguments are mentioned
deposit_calculator(deposit_amount=1000, actual_balance=13570)
# # Here the keyword for both argument are given by swapping it to each other's place which is positional argument
deposit_calculator(actual_balance=12750, deposit_amount=500)

# # Here is example for one with keyword args
deposit_calculator(1000, deposit_amount=1000)    # it will raise an error as two value passed for single argument

# Here is an example for one with keyword args and with positional argument
deposit_calculator(1000, actual_balance=12000)


# Example for Arbitrary argument -> non-keyword argument and keyword argument

def test(*number):
    total = 0
    for n in number:
        total = total + n
    print(total)
    print("output for *number : ", *number)
    print(number, "\n")


test()    # print *number will give nothing as output and number will give empty tuple.
test(1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)


# when we give ** before argument name then which denotes key value arguments
def intro(s, d='1', /, *, data):
    print("{} ) {} is {} ".format(d, data, s))


intro('harini', data="name")


# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1))
# print(f(2))
# print(f(3))
#
#
# def a(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L
#
# print(a(1))
# print(a(2))
# print(a(3))


"""
Example of Anonymous function 
"""

# lambda functions
square = lambda number: number ** 2

print(square(5))


"""
Example of Enumerate function 
"""

grocery_list = ['biscuits', 'milk', 'coffee']
enumerateGrocery = enumerate(grocery_list)

print(type(enumerateGrocery))

# printing iterable with next()
print(next(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery_list, 10)
print(list(enumerateGrocery))


# list_of_employee = []


# def get_details():
#     list_details = []
#     while True:
#         list_size = int(input("Enter number of details you want to create : \n"))
#         for i in range(0, list_size):
#             employee_name = input("Enter employee name : \n")
#             role = input("Enter employee role : \n")
#             list_details.append([employee_name, role,])
#         another_employee_list = input("Do you want to add another details? (YES/NO): ")
#         capitalize_list = [l.capitalize() for l in another_employee_list]
#         list_to_str = ''.join([str(elem) for elem in capitalize_list])
#         if list_to_str in ('NO','N','NOPE','NOT'):
#             break
#     return dict(enumerate(list_details,1))
#
#
# def employee_details():
#     while True:
#         print("Enter 1 - add\n2 - display entire employee list\n"
#               "Press any other number to exit !")
#         choice = input("Enter your choice : \n")
#         match choice:
#             case '1':
#                 value = get_details()
#                 list_of_employee.append(value)
#             case '2':
#                 print("Employee List : \n")
#                 print(list_of_employee)
#         another_calculation = input("Do you want to continue? (YES/NO): ")
#         capitalize_list = [l.capitalize() for l in another_calculation]
#         list_to_str = ''.join([str(elem) for elem in capitalize_list])
#         if list_to_str == 'NO':
#             break
#
#
# print(employee_details())

# salary_list = [500, 700, 456, 200, 150]
# employee_list = ['harini', 'siva', 'moni']
#
#
# def calculate_salary(salary):
#     return round((salary * 30) - ((salary * 30) / 44),2)
#
#
# total_salary_list = list(map(lambda salary: round((salary * 30) - ((salary * 30) / 44), 2), [400, 600, 1000]))
# list_salary = list(total_salary_list)
# map_employee_salary = list(zip(employee_list, total_salary_list))
# print(map_employee_salary)
# print(*map(calculate_salary, salary_list))
# employee_salary = list(map_employee_salary)

#
# def salary_filtering(list_salary):
#     for element in list_salary:
#         if element > 15:
#             return element
#
#
# salary_filter = filter(salary_filtering,total_salary_list)
# print(list(salary_filter))

# employee_details = {'name': 'harini', 'id': 2, 'role': 'trainee'}
# list_fruits = ['apple', 'Banana', 'pineapple']
# set_sample = {'1', '10', (1, 2, 3), '10'}
# employee_name_list = [employee for employee in employee_details.values()]    # prints only the value of dictionary
# fruit_name_list = [fruits.upper() for fruits in list_fruits]    # change element to uppercase by iterating list
# sample_list = [sample for sample in set_sample]
# print("list to list : ")
# print(fruit_name_list)
# print("dictionary to list : ")
# print(employee_name_list)
# print("set to list : ")
# print(sample_list)
