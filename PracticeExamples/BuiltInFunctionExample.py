"""
This will have example of built-in functions like map, zip,
filter
"""
from functools import reduce

# print(list(map(add, [1, 2, 3], [4, 5, 6])))

# Example for zip
player_list = ['sara', 'madhu', 'siva', 'vikash']
points_list = [2,3,2]

print("map as dictionary:")
print(dict(zip(player_list, points_list)), "\n")
print("map as list:")
print(list(zip(player_list, points_list)), "\n")


# Example program for map :
def add(first_number, second_number):
    total = first_number + second_number
    return total


print("map examples:")
print(list(map(add, [1, 2, 3], [4, 5, 6])), "\n")
print(list(map(add, [1, 2, 3], [4, 5])), "\n")
print(*map(add, [1, 2, 3], [4, 5,6]), "\n")


def multiply(number):
    total = number[0] * number[1]
    return total


print("zip inside map:")
print(list(map(multiply, list(zip([1, 2, 3], [4, 5, 6])))), "\n")

print("map inside zip:")
print(list(zip(map(multiply, list(zip([1, 2, 3], [4, 5, 6]))), map(add, [1, 2, 3], [4, 5, 2]))), "\n")

print("filter inside zip and lambda inside filter:")
a = [1, 2, 2, 5, 3, 4, 5, 6, 7]
b = [2, 3, 4, 2, 3, 4]
print(list(zip(filter(lambda c: c % 2 == 0, a), filter(lambda d: d != 3, b))), "\n")
# new = [x for x in a if x % 2 == 0]
# new_list = [y for y in b if y != 3]


def new(a):
    for x in a:
        if x % 2 == 0:
            yield x + x


def new_list(b):
    for y in b:
        if y != 3:
            yield y + y


print("filters inside zip :")
print(list(zip(filter(new, a), filter(new_list, b))))


# list1 = [2,3,4,5,6,6,7,8,3]
# filter_example = [lambda x: ]

# salary_list = [500, 700, 456, 200, 150]
#
#
# def calculate_salary(salary):
#     salary_without_tax = salary * 30
#     tax_reduction = salary_without_tax / 44
#     final_salary = salary_without_tax - tax_reduction
#     return round(final_salary,2)
#
#
# print(list(map(calculate_salary, salary_list)))

print("filter inside map:")
a = [1, 2, 2, 5, 3, 4, 5, 6, 7]
b = [2, 3, 4, 2, 3, 4]
print(list(map(lambda c, d: c + d, filter(lambda c: c % 2 == 0, a), filter(lambda d: d != 3, b))), "\n")

print("filter inside map:")
a = [1, 2, 2, 5, 3, 4, 5, 6, 7]
b = [2, 3, 4, 2, 3, 4]
print(list(map(lambda c, d: c + d, filter(lambda c: c % 2 == 0, a), filter(lambda d: d != 3, b))), "\n")

print("map inside filter:")
a = [1, 2, 2, 5, 3, 4, 5, 6, 7]
b = [2, 3, 4, 2, 3, 4]
print(set(filter(lambda element: element % 2 == 0, map(lambda first_number, second_number:
                                                       first_number * second_number, a, b))),"\n")
#
# print("zip inside map with zip as function:")
# print(list(map(zip, [1, 2, 3], [4, 5, 6])), "\n")

a = [1, 2, 3, 1, 2, 5, 7, 2, 3, 2]
dictionary = {x: a.count(x) for x in a}
print(dictionary)

# dic = {}
# for i in a:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
#
#
# print(dic)

# print("zip inside map:")
# print(list(map(multiply, [(1, 2), (3, 4), (5, 6)])), "\n")
#


def my_min_func(a, b):
    return a if a < b else b


print(reduce(my_min_func, [1, 2, 3, 4, 5, 6], 10))


# Example for recursion
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


print(reverse('python'))


def is_palindrome(string):
    if len(string) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome('harini'))
print(is_palindrome('radar'))

a = float(0.3)
b = float(round(0.1 + 0.2, 1))
print(a == b)


# def findmin(list_a, n):
#     if n == 1:
#         return list_a[0 ]
#
#     else:
#         return min(list_a[n - 1], findmin(list_a, n - 1))
#
#
# A = [1, 4, 24, 17, -5, 10, -22]
# n = len(A)
#
# print(findmin(A, n))




# def plus_one(number):
#     return number + 1
#     def function_call(function):
#         number_to_add = 5
#         return function(number_to_add)
#
#
# print(function_call(plus_one))