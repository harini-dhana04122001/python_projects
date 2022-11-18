"""Numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
Result = [Number for list1 in Numbers for Number in list1 if Number % 2 == 0]
print(Result)"""


# List Comprehension
"""from constants import constant


price_list = [1000, 2500, 1200, 3000, 4000]
customer_name = ['sara', 'mohini', 'divya', 'madhu', 'latha']

employee_details = [constant.DISCOUNT for price in price_list if (price < 10000) and (price > 2200)]


print(dict(zip(customer_name, zip(price_list, employee_details))))"""

# Example for map and zip
"""def percentage_calculator(first_number, second_number):
    percentage = (first_number / second_number) * 100
    print((first_number / second_number)*100)
    return percentage


def gift_provider(marks_scored):
    mark_percentage = percentage_calculator(marks_scored, 500)
    if (mark_percentage > 55.0) and (mark_percentage < 74.9):
        return "C Grade"
    elif (mark_percentage > 75.0) and (mark_percentage < 89.0):
        return "B grade"
    elif mark_percentage >= 90.0:
        return "A grade"


student = ['nivi', 'megha', 'deepthi']
marks_scored = [450, 470, 400]
print(list(zip(student,map(gift_provider,marks_scored))))"""

# Example 1 for Dictionary
"""input_list = [{1, 2, 3, 4}, {2, 5, 6, 7, 7}]

comprehension = {var: var * 2 for lists in input_list for var in lists if var >= 2}

print("Output List using list comprehensions:", comprehension)

input_list = [{1, 2, 3, 4}, {2, 5, 6, 7, 7}]

new = {}
for lists in input_list:
    for var in lists:
        if var >= 2:
           new = {var: var * 2}

comprehension = {var: var * 2 for lists in input_list for var in lists if var >= 2}

print("Output List using list comprehensions:", comprehension)"""

# Example 2 for Dictionary
"""input_list = [1, 2, 3, 4]
another_list = {'hari', 'moni', 'siva'}

comprehension = {key: value for key, value in zip(input_list, another_list)}

print("Output List using list comprehensions:", comprehension)"""

# # Example 3 for Dictionary
"""input_list = [1, 2, 3, 4]
another_list = {'hari', 'moni', 'siva'}

comprehension = {key: value for key, value in zip(input_list, another_list)}

print("Output List using list comprehensions:", comprehension)"""


# nested dictionary comprehension
data = [
    {
        'id': 1,
        'role': 'Front-end',
        'name': 'Siva'
    },
    {
        'id': 2,
        'role': 'Python',
        'name': 'Moni'
    },
    {
        'id': 3,
        'role': 'Python',
        'name': 'Harini'
    },
    {
        'id': 4,
        'role': 'Rpa',
        'name': 'Dhivya'
    }
]
data = {role: {d["id"]: d["name"] for d in [i for i in data if i["role"] == role]}
        for role in set((j["role"] for j in data))}

print(data)


# Example for generator comprehension
# # def demo():
# new = (value for value in reversed(range(1, 10, 2)))
#         # yield value
#
# print(type(new))
# for i in new:
#     print(i)


# list1 = [1,2,3,4,5]
#
# add = [value for value in list1 if value == 6]
#
# print(add)

# list = [[1,2,3],[1,2],[1],[1,2,3,4]]
# for x,y,a in list:
#     print(x,y)

# b = list,
# print(type(b))