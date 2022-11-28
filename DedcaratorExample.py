"""
This is an example program for decorator in python
Args: func (add function is passed). (<class 'function'>)
Return: function object of the name_printer and star_wrapper (<class 'function'>)
"""


def name_printer(func):
    def wrapper(*args):
        print("Function that is started running : " + func.__name__)
        func(*args)
    return wrapper


def star_wrapper(func):
    def star(*args):
        print('*' * 30)
        func(*args)
        print('*' * 30, "\n")
    return star


@name_printer
@star_wrapper
def add(*args):
    tot_sum = 0
    for arg in args:
        tot_sum += arg
    print("result = " + str(tot_sum))


# ex 1
add(1, 2)

# ex 2
add(1, 2, 3)

# ex 3
add(1, 2, 3, 4)


