"""
Work wants an inventory app that:
    Stores Data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            cond
"""
from models.item import Item

next_id = 0
items = []
# TODO Make a menu print out showing options
def menu():
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

# List all Items
def list_items():
    for item in items:
        print(item)

# Add New Item
def new_item():
    global next_id
    global items

    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id

    next_id += 1

    tmp = Item(item_id, name, cond)
    items.append(tmp)


# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass

# Make the menu questions that grab the data 
def main():
    while True:
        menu()
        choice = input("> ")

        if choice == "1":
            list_items()
        elif choice == "2":
            new_item()
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5": # Exit
            exit()
        else:
            input("Invalid Input!\n(Press Enter to try again)")


# Make the File Saving stuff

if __name__ == "__main__":
    main()