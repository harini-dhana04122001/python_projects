from collections import UserDict


class MyData(UserDict):
    def __init__(self, s=None):
        super().__init__()
        self.data = s

    def reverse_iter(self):
        for i, j in reversed(list(self.data.items())):
            print(i, ":", j)

    def iterate_dict(self):
        for i, j in self.data.items():
            print(i, ":", j)


mydict = MyData({'x': 10, 'y': 20})

# creating additional method for UserDict
print("iterate in reverse order : ")
mydict.reverse_iter()
print("iterate dictionary : ")
mydict.iterate_dict()

# Deleting From Dict
mydict.pop('x')
print("mydict after deletion : ", mydict)
