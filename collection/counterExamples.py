from collections import Counter


""" Counter Example """
String1 = 'Encyclopedia'
new_count_string = Counter(String1.lower())
print(new_count_string)
list_count = Counter([1, 2, 2, 3, 4, 1, 5, (6, 7), 2, 5, (6, 7)])
print("count of list : ", list_count)
# c = Counter({'red': 5, 'blue': 2, 'violet': 5})
print("Most common occurrence : ", list_count.most_common(2))
print("Sum of all count : ", list_count.total())
print("display the items in dictionary : ", list_count.items())
# print("clear all keys : ", list_count.clear())
print("converting a dict counter to set : ", set(list_count))
counter1 = Counter([1, -2, -3, 2, 3, 4])
counter2 = Counter([1, 3, 1, 2, 3, 4])
counter1.subtract(counter2)
print(counter1)
print(+counter1)  # eliminate negative and zero values count



