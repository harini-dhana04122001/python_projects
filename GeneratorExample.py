import csv

filename = r'C:\Users\LENOVO\Documents\csv\temperature.csv'


def csv_reader():
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        rows = (row for row in csvreader)
        yield rows


def celsius_to_fahrenheit():
    new_list = csv_reader()
    fahrenheit = (round((float(i) * 1.8) + 32, 2) for row in new_list for element in row for i in element)
    yield fahrenheit


new = celsius_to_fahrenheit()
print("Temperature from celsius to fahrenheit : ")
for i in new:
    for j in i:
        print(j)
