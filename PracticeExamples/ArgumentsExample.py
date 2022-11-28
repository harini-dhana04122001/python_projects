"""
This file is to practice examples for different types of argument
it covers all these four types of argument which are
default argument, keyword argument, positional
"""


# Default argument examples
# It is not possible to pass a non-default argument after a default argument but its possible to pass a
# Default argument after non-default argument.
def show_details(name='harini', *, age):
    print("name of the employee is ", name, "and their age is ", age, "\n")


show_details('Harini')
show_details(age=21)    # output of age will be 21 as argument for age is given


# Positional and Keyword argument examples
def deposit_calculator(deposit_amount, actual_balance):
    new_balance = actual_balance + deposit_amount
    print("current balance is ", new_balance, "\n")


# Here the keyword for both arguments are mentioned
deposit_calculator(deposit_amount=1000, actual_balance=13570)
# Here the keyword for both argument are given by swapping it to each other's place which is positional argument
deposit_calculator(actual_balance=12750, deposit_amount=500)

# # Here is example for one with keyword args
# deposit_calculator(1000, deposit_amount=1000)    # it will raise an error as two value passed for single argument

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
test(1, 2, 3, 4)


# when we give ** before argument name then which denotes key value arguments
def intro(**data):
    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Product="Shampoo", Price=270.20, Discount=20)
intro(Firstname="Saira", Lastname="Begum", Email="saira@gmail.com", Age=21)
