from collections import UserList


class MyData(UserList):
    def __init__(self, s=None):
        super().__init__()
        self.data = s

    def reverse_iter(self):
        for i in reversed(list(self.data)):
            print(i)

    def iterate_dict(self):
        for i in self.data:
            print(i)


mylist = MyData([10, 20, 30])

mylist.append(5)
print("Insertion..")
print(mylist)

print("iterate in reverse order : ")
mylist.reverse_iter()
print("iterate list : ")
mylist.iterate_dict()
