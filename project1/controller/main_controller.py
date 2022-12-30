import csv
from constants.constant import PASSENGER_FILE_NAME
from project1.booking_details import BookingDetails
from project1.controller.passenger_controller import add_passenger_details, display_details_by_id, \
    display_details_by_contact_number
from project1.passenger_details import PassengerDetails



booking_details_ = dict()
bookings = BookingDetails()
passenger = PassengerDetails()


def main():
    is_working = True
    while is_working:
        print('Enter 1 to add passenger details\nEnter 2 to display passenger details')
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                add_passenger_details()

            case '2':
                with open(PASSENGER_FILE_NAME, 'r+') as details:
                    csv_read = csv.reader(details)
                    for i in csv_read:
                        print(i)

            case '3':
                display_details_by_id()

            case '4':
                display_details_by_contact_number()

            case _:
                print("End of Service!")
                is_working = False


if __name__ == "__main__":
    flag = True
    while flag:
        try:
            main()
            flag = False
        except Exception as ex:
            print(f"\n--------- Exception handled : {ex} ----------")