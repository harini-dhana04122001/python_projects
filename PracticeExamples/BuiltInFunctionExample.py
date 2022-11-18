"""
This will have example of built-in functions like map, zip,
filter
"""


# Example program for map :
def add(first_number, second_number):
    total = first_number + second_number
    return total


print(list(map(add, [1, 2, 3], [4, 5, 6])))
print(list(map(add, [1, 2, 3], [4, 5])))
print(*map(add, [1, 2, 3], [4, 5,6]))






# print(list(map(add, [1, 2, 3], [4, 5, 6])))
#
# # Example for zip
# player_list = ['sara', 'madhu', 'siva', 'vikash']
# points_list = [2,3,2]
#
# print(dict(zip(player_list, points_list)))
# print(list(zip(player_list, points_list)))


