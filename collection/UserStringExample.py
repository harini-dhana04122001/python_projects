from collections import UserString

d = [12344, 123]

# Creating an UserDict
userS = UserString(d[0])
print('1: ', userS.data)

# Creating an empty UserDict
userS = UserString("")
print('2: ', userS.data)


class MyString(UserString):

    # Function to append to string
    def append(self, s):
        self.data += s

    # Function to remove from string
    def remove(self, to_replace):
        self.data = self.data.replace(to_replace, "")


# Driver's code
s1 = MyString("hello")
print("Original String:", s1.data)

# Appending to string
s1.append("s")
print("String After Appending:", s1.data)

# Removing from string
s1.remove("e")
print("String after Removing:", s1.data)
