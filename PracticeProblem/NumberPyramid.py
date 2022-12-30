def number_pyramid(num):
    for i in range(num):
        if i == num-1:
            print(" " * i + str(num-i) + " " * (2 * (num - 1 - i) - 1))
        else:
            print(" " * i + str(num - i) + " " * (2 * (num - 1 - i) - 1) + str(num - i))


input_number = int(input("Enter a number : "))
number_pyramid(input_number)
