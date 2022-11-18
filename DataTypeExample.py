class ListExample:
    grocery_list = []


def add_list(grocery_list):
    while True:
        list_size = int(input("Enter list range : "))
        for i in range(0, list_size):
            item_id = input("Enter item id : ")
            item_name = input("Enter item name : ")
            quantity = input("Enter item quantity : ")
            grocery_list.append({item_id: (item_name, quantity)})
        another_grocery_list = input("Do you want to add another grocery? (YES/NO): ")
        capitalize_list = [l.capitalize() for l in another_grocery_list]
        list_to_str = ''.join([str(elem) for elem in capitalize_list])
        if list_to_str == 'NO':
            break
    return grocery_list


def display_by_id(grocery_list):
    while True:
        item_id = input("Enter item id : ")
        for grocery in grocery_list:
            print(grocery.get('A'))
        another_grocery_list = input("Do you want to display another grocery list? (YES/NO): ")
        capitalize_list = [l.capitalize() for l in another_grocery_list]
        list_to_str = ''.join([str(elem) for elem in capitalize_list])
        if list_to_str == 'NO':
            break


def remove_list(grocery_list):
    item_id = input("Enter item id : ")
    item_name = input("Enter item id : ")
    quantity = input("Enter item id : ")
    for grocery in grocery_list.copy():
        if grocery.get(item_id) == (item_name, quantity):
            grocery_list.remove(grocery)
            print("grocery details are deleted !")
            break
    return grocery_list


def grocery_details(grocery_list):
    while True:
        print("Enter 1 - add\n2 - display entire grocery list\n3 - display specific item\n"
              "4 - delete a grocery from list\nPress any other number to exit !")
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                add_list(grocery_list)
            case '2':
                print('-------- Display grocery list -------- \n')
                print(grocery_list)
            case '3':
                print('------ Display grocery with given id ------ \n')
                display_by_id(grocery_list)
            case '4':
                remove_list(grocery_list)
        another_calculation = input("Do you want to continue? (YES/NO): ")
        capitalize_list = [l.capitalize() for l in another_calculation]
        list_to_str = ''.join([str(elem) for elem in capitalize_list])
        if list_to_str == 'NO':
            break


print(grocery_details(ListExample.grocery_list))



