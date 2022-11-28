import csv

filename = r'C:\Users\LENOVO\Documents\csv\temperature.csv'


def csv_reader():
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        rows = (row for row in csvreader) # generator comprehension is performed here
        yield rows


def celsius_to_fahrenheit():
    new_list = csv_reader()
    # nested generator comprehension
    fahrenheit = (round((float(i) * 1.8) + 32, 2) for row in new_list for element in row for i in element)
    yield fahrenheit      # it is going to return the value by converting celsius to fahrenheit


fahrenheit_generator = celsius_to_fahrenheit()
print("Temperature from celsius to fahrenheit : ")


def display_one_by_one():
    flag = True
    for temperature in fahrenheit_generator:
        while flag:
            choice = int(input("Enter 1 to continue displaying the value \n Enter 2 to break \n"
                               "Enter your choice : "))
            if choice == 1:
                print(next(temperature))
            elif choice == 2:
                break


print(display_one_by_one())

# print(0.1+0.2 == 0.3)



