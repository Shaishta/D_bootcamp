#Exercise 1 : Restaurant Menu Manager
#Part 2
from exercisexp import MenuItem

def load_manager():
    new_menu = MenuItem()
    return new_menu

def show_user_menu():
    print('''
    Menu
    1. Add an item
    2. Delete an item
    3. View the menu
    4. Exit''')
    ans = input('Please enter choice from 1 to 4: ')
    if ans == '1':
        return add_item_to_menu()
    elif ans == '2':
        return remove_item_from_menu()
    elif ans == '3':
        return show_restaurant_menu()
    elif ans == '4':
        print('See you soon! Goodbye')
        return
    else:
        print("Error. Please try again!")
        return show_user_menu()

def add_item_to_menu():
    name = input('Enter the name of the item: ')
    price = int(input('Enter the price of the item: '))
    item = MenuItem(name, price).save()
    print('item was added successfully')
    return show_user_menu()

def remove_item_from_menu():
    name = input('Enter the name of the item: ')
    item = MenuItem(name).delete()
    if MenuItem().get_by_name(item) == None:
        print('item was deleted')
    else:
        print("error")
    return show_user_menu()

def show_restaurant_menu():
    print(MenuItem().all())
    return show_user_menu()

show_user_menu()
