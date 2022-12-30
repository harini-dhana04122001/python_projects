# from threading import Thread
#
#
# def name_printer(func):
#     print("2")
#
#     def wrapper(*args):
#         print("3\n")
#         print("Function that is started running : " + func.__name__, "\n")
#         func(*args)
#         print("4")
#         print("decorator ends here\n")
#     return wrapper
#
#
# print("1")
#
#
# @name_printer
# # a custom function that blocks for a moment
# def task(a, b):
#     print("5")
#     # display a message
#     c = (a*b)/2
#     return c
#
#
# # create a thread
# thread = Thread(target=task, args=(3, 4))
# thread2 = Thread(target=task, args=(5, 6))
# # run the thread
# thread.start()
# thread2.start()
# thread.join()

import threading
import time


def func_add(a, b):
    time.sleep(2)
    print(threading.enumerate())
    print("thread count : ",threading.active_count())
    print("add : ", a + b)


def func_sub(a, b):
    time.sleep(5)
    print(threading.enumerate())
    print("thread count : ",threading.active_count())
    print("sub : ", a - b)


def func_mul(a, b):
    time.sleep(1)
    print(threading.enumerate())
    print("thread count : ",threading.active_count())
    print("mul : ", a * b)


def func_div(a, b):
    print(threading.enumerate())
    print("thread count : ",threading.active_count())
    print("div : ", a / b)


thread_a = threading.Thread(target=func_add, args=(10000, 70000))
thread_b = threading.Thread(target=func_sub, args=(10000, 70000))
thread_c = threading.Thread(target=func_mul, args=(10000, 70000))
thread_d = threading.Thread(target=func_div, args=(10000, 70000))
print(threading.active_count())
thread_c.start()
thread_d.start()
thread_a.start()
thread_b.start()


thread_d.join()
thread_b.join()
thread_a.join()
thread_c.join()


# Program to count active threads
# active_count() method from Threading Module
# import threading
# import time


# # Methods for three threads..
# def thread1_Subroutine(i):
#     time.sleep(2)
#     print(threading.enumerate())
#
#     print("Thread-1: Number of active threads:", threading.active_count())
#     print('Thread 1 Value:', i)
#
#
# def thread2_Subroutine(i):
#     print(threading.enumerate())
#     print("Thread-2: Number of active threads:", threading.active_count())
#     print('Thread 2 Value:', i)
#
#
# def thread3_Subroutine(i):
#     time.sleep(5)
#     print(threading.enumerate())
#     print("Thread-3: Number of active threads:", threading.active_count())
#     print("Thread 3 Value:", i)
#
#
# # Creating sample threads
# thread1 = threading.Thread(target=thread1_Subroutine, args=(100,), name="Thread1")
# thread2 = threading.Thread(target=thread2_Subroutine, args=(200,), name="Thread2")
# thread3 = threading.Thread(target=thread3_Subroutine, args=(300,), name="Thread3")
# print("START: Current active thread count: ", threading.active_count())
# # Calling start() method to initialize execution
# thread1.start()
# thread2.start()
# thread3.start()
# thread3.join()  # Wait for thread-3 to join.
