with open("C:/demo_txt.txt", "r+") as file:
    data = file.read().replace("Ideas2IT", "IT Company")
    file.seek(0)
    file.write(data)
    file.seek(0)
    print(file.read())

dict1 = {1: 'a', 2: 'b', 3: 'c'}
for key in dict1.copy():
    if key == 2:
        del dict1[2]

print(dict1)


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class B(A):

    def __init__(self, *args):
        # args1 = list(args)
        super().__init__(args[0], args[1])
        self.c = self.a
        self.d = self.b

    def display(self):
        return f'{self.c} and {self.d}'


obj1 = B(2, 3)
print(obj1.display())

# list1 = [1,2,3,-4,5,-3]
# for i in list1:
#     if i < 0:
#         print(i)


# a = [1,2,3,4,5]
# new = filter(lambda x: x > 3, a)
# print(list(new))
#
# # list1 = [1, 2, 3, 4, 5]
# # list2 = [6, 7, 8, 9, 10]
# set1 = {1, 2, 3, 4}
# set2 = {4, 3, 2, 5}
# print(set1.intersection(set2))

# class A:
#     e = 10
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def add(self):
#         return self.a + self.b
#
# class B(A):
#
#     def __init__(self):
#         # args1 = list(args)
#         super().__init__()
#         self.c = self.e
#         # self.d = self.b
#
#     def display(self):
#         return f'{self.add()} '
#
#
# obj1 = B()
# print(obj1.display())
from collections import ChainMap

a = {"ajay": {"tamil": 35, "english": 45, "maths": 60}, "josh": {"tamil": 38, "english": 48, "maths": 63},
     "arun": {"tamil": 36, "english": 46, "maths": 61}, "siva": {"tamil": 37, "english": 47, "maths": 62}
     }

dict1 = {}
for i, j in a.items():
    count = 0
    for k in j.keys():
        count = count + j[k]
    dict1.setdefault(i, count)
    print(count)
print(dict1)
display = sorted(dict1.items(), key=lambda x: x[1], reverse=True)

print(display)





