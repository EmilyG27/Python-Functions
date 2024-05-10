def main_menu():
    while True:

        menu = input("'add', 'remove', or 'view'? ")

        if menu == "add":
            add_item()
        elif menu == "remove":
            remove_item()
        elif menu == "view":
            display_list()
        else:
            print("Invalid selection. Please choose 'add', 'remove', or 'view'. ")

shopping_list = []

def add_item():
    item = input("Enter item: ")
    shopping_list.append(item)
    print(item + " has been added to the shopping list.")

def remove_item():
    item = input("Which item do you want to remove? ")
    shopping_list.remove(item)
    print(item + " has been removed.")

def display_list():
    for i in shopping_list:
        print(i + ", ")

main_menu()
