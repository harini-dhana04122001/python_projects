from constants import sample
# Simple average program
""" Variable Name and function name should be in lower
    case when there are multiple names
    use underscore """
# Calling of the func should be after two space lines.
# One space line for differentiating two steps.
""" Leave one space after comma, colon 
    and semicolon but not before """


# def demo_func(a, b):
#     total = a + b
#
#     average = total / 5
#     return average
#
#
# print(demo_func(5, 6))


# Add some extra indentation on the conditional continuation line.
# No extra indentation is needed for normal function argument.
# def demo_sum(
#         first_number, second_number,
#         third_number, fourth_number):
#     if (first_number > second_number and
#             third_number > fourth_number):
#         answer = first_number * second_number \
#             * third_number * fourth_number
#         return answer


# list1 = [
#     1, 2, 3
#     ]
#
#
# list2 = [
#     1, 2, 3
# ]


def login_message(message):
    name = input('Enter your name : ')
    password = input('Enter a password :')
    print('HI', name, 'WELCOME TO ', message)


login_message(sample.COMPANY_NAME)

# tuple3 = ("apple", "mango")
# tuple3[1].append("mango")
# print(tuple3)

# fruits = ["mango", "banana"]
# print(id(fruits))
# vegetables = input("Enter a veggie name : ")
# fruits.append(vegetables)
# print(fruits)
# print(id(fruits))
# fruits.append("tomato")
# print(fruits)
# print(id(fruits))

# nestedTuple = ('hello', [1, 2, 3], (4, 5, 6))
# print(nestedTuple[0][2])
# print(nestedTuple[2][2])

list2 = [('harini', 1), ('siva', 2), ('dhanesh', 3)]
list2.append(('divya', 4))
print(list2)