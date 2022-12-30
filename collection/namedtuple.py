from collections import namedtuple

Trainee = namedtuple('Trainee', ['name', 'role', 'current_task'], defaults=['','',''])


# def getting_inputs():
#     inputs = int(input("number of details you want to enter : "))
#     for i in range(inputs):
#         name = input("enter your name : ")
#         role = input("enter your role : ")
#         current_task = input("enter your current task : ")
#         trainee_details = Trainee._make([name, role, current_task])
#         print(trainee_details.name)  # printing out just the name of the instance
#         print(trainee_details._asdict())  # prints the details as dictionary
#         trainee_details = trainee_details._replace(role='python trainee')
#         print(trainee_details)
#         print(trainee_details._fields)
#
#
# getting_inputs()

Person = namedtuple("Person", ['name', 'age', 'height', 'weight'], defaults=["67"])
# NewPerson = namedtuple("NewPerson", [*Person._fields, "weight"])
#
""" Using _field to map values to namedtuple """
# person1 = NewPerson("Jane", 26, 1.75, 67)
# print(person1)
""" Using Zip to map values to namedtuple """
person1 = Person("Jane", 26, 1.75)
for field, value in zip(person1._fields, person1):
    print(field, "->", value)

print(Person._field_defaults)
