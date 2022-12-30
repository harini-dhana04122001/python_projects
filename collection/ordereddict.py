from collections import OrderedDict

""" OrderedDict Examples """
numbers = OrderedDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3
print("ordered dict output", numbers)
numbers.pop('one')
numbers["one"] = 1
print("Value after reinserting a value : ", numbers)
numbers.move_to_end("one", last=False)
print(numbers)
new_dict = dict()
new_dict["1"] = 'harini'
print(new_dict)
# for number in reversed(numbers):
#     print(number, '->', numbers[number])
physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")
biologists = OrderedDict(darwin="1809-1882", mendel="1822-1884")

scientists = physicists | biologists
print(scientists)

physicists1 = dict(newton="1642-1726", einstein="1879-1955")
biologists1 = dict(darwin="1809-1882", mendel="1822-1884")
scientists1 = physicists | biologists
print(scientists1)


