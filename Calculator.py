"""
This is a program which perform basic arithmetic operation
such as addition, subtraction, multiplication, division
"""


def calculator():
    print("1 - addition /n2 - subtraction/n3 - multiplication/n4 - division")
    while Calculator.flag:
        choice = int(input("Enter a choice : "))
        first_number = int(input("Enter a first number : "))
        second_number = int(input("Enter a second number : "))
        if choice == 1:
            print("Answer of addition is : ", add(first_number, second_number))

        elif choice == 2:
            print("Answer of subtraction is : ", sub(first_number, second_number))

        elif choice == 3:
            print("Answer for multiplication is : ", multiplication(first_number, second_number))

        elif choice == 4:
            print("Answer for division is : ", division(first_number, second_number))

        else:
            print("Invalid Input")

        # check if user wants another calculation

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'no':
            Calculator.flag = False
            break  # break the while loop if answer is no


def add(*args):
    total = 0
    for numbers in args:
        total = total + numbers
    return total


def sub(first_number, second_number):
    total = first_number - second_number
    return total


def multiplication(first_number, second_number):
    total = first_number * second_number
    return total


def division(first_number, second_number):
    total = first_number / second_number
    return total


class Calculator:
    name = input("Enter your name : ")
    print("hello ", name, "!")
    flag = True


calculator()



