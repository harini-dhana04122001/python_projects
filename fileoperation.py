import csv
import re
from csv import writer

logs = open("C:\\log_file.txt")     # this is the log file


def get_warning():
    with open(r'C:/warning.csv', "r+") as warning:
        file = csv.writer(warning)
        header = ("Timestamp", "Application Name", "Status", "Description", "Code")
        file.writerow(header)
        for log in logs:
            if "Warning" in log:
                columns = re.split(',|: |    ', log)
                warning_log = (columns[0], columns[5], "Warning", columns[7].replace("\n", ""), "code")
                file.writerow(warning_log)
        read_file = csv.reader(warning)
        for i in read_file:
            print(i)


def get_failure():
    with open('C:\\failed.csv', "r+") as failed:
        # print(type(failed))  # <class '_io.TextIOWrapper'>
        file = csv.writer(failed)
        header = ("Timestamp", "Application Name", "Status", "Description", "Code")
        file.writerow(header)
        for log in logs:
            if "Failed" in log:
                fail = re.split(',|    ', log)
                failed_log = (fail[0], fail[5], "Failed", fail[6].replace("\n", ""), "code")
                file.writerow(failed_log)
        read_file = csv.reader(failed)
        for i in read_file:
            print(i)


print("1. warnings")
print("2. failed")
choice = int(input("Enter choice"))
match choice:
    case 1:
        get_warning()
    case 2:
        get_failure()
    case _:
        print("end....")

# # new_file = open('C:\\Users\\LENOVO\\new_file1.txt', 'w')




