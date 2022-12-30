"""
This function will calculate average of the marks that is being passed.

Args : function - have the value of both function and argument - which can be used
       to inner function through closure
Return : wrapper(function) - returns the calculated average
"""


def average_marks(function):
    def wrapper(*args):
        marks = 0
        for mark in args:
            marks += mark    # overall marks gets calculated here
        print("total marks without average : ", marks)
        average = marks/5
        function(average)    # goes to grade_them function inside grade function
        print("function ends here!")
    return wrapper


def grade(function):
    def grade_them(average):
        if 50.0 < average < 60.0:
            return function("C grade")
        elif 60.0 < average < 70.0:
            return function("B grade")
        elif 75.0 < average < 85.0:
            return function("A grade")
        elif 85.0 < average:
            return function("S grade")
        else:
            return function("fail")
    return grade_them


"""
prints the grade for given marks
Args: grades(string) - grades that need to be displayed
"""


# When value is passed it will load grade function first and then average_marks gets loaded
# After which it follows the order of syntactic sugar
@average_marks
@grade
def total_marks(grades):
    print("Marks garde : ", grades)   # output is printed after the grade function returns the value


mark1, mark2, mark3, mark4, mark5 = input("Enter a five value with comma in between : ").split(',')
total_marks(int(mark1), int(mark2), int(mark3), int(mark4), int(mark5))


"""
Example for first class function(functions that can be passed as argument)
"""


# def add(number_1, number_2):
#     return number_1 + number_2
#
#
# def multiply(number_1, number_2):
#     return number_1 * number_2
#
#
# def calculator(operations):
#     a = int(input("Enter a number : "))
#     b = int(input("Enter another number : "))
#     return operations(a, b)
#
#
# print("addition of 12 and 12 is ", calculator(add))
# print("multiplication of 12 and 12 is ", calculator(multiply))

"""
Example for inner function(nested function)
"""


# def calculate_salary():
#     salary = float(input("Enter a salary : "))
#
#     def calculate_pf():
#         first_step = (2*salary)/100
#         tax = first_step/100
#         return tax
#     tax1 = calculate_pf()
#     return salary - tax1
#
#
# print(calculate_salary())


"""
This is an example program for decorator in python
Args: func (add function is passed). (<class 'function'>)
Return: function object of the name_printer and star_wrapper (<class 'function'>)
"""


# def name_printer(func):
#     print("2")
#
#     def wrapper(*args):
#         print("3")
#         print("Function that is started running : " + func.__name__)
#         func(*args)
#         print("4")
#         print("decorator ends here\n")
#     return wrapper
#
#
# def star_wrapper(func):
#     print("5")
#
#     def star(*args):
#         print("6")
#         print('*' * 40)
#         func(*args)
#         print('*' * 40)
#         print("7")
#     return star
#
#
# @name_printer
# @star_wrapper
# def add(*args):
#     print("0")
#     tot_sum = 0
#     for arg in args:
#         tot_sum += arg
#     print("1")
#     return tot_sum
#
#
#
#
# add(1, 2)
#
# # ex 2
# add(1, 2, 3)
