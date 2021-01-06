"""
Work wants an inventory app that:
    Stores Data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            cond
"""
from models.item import Item # and import statement to make code form othe files available

next_id = 0
items = []

def menu(): # prints the menu options for the user
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

def list_items(): # writes all the items to the termial 
    for item in items:
        print(item)

def new_item(): # gets user to input for all need fields for an item
    global next_id #allows us access to the next_id number
    global items

    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id # uses the global counter to give a unique id to each item

    next_id += 1 # updates the id with new value so next one is 1 more

    tmp = Item(item_id, name, cond) # builds an item/stores it i tmp
    items.append(tmp) # adds item to global items array 


# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass

def main(): # starts the program off, holds the loop until exit.
    while True:
        menu() # prints the options to the terminal 
        choice = input("> ") # takes users choice

        # the conditional options: hands off the work to function above.
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
        else: # user gave us bad input we let them know then loop again 
            input("Invalid Input!\n(Press Enter to try again)")


# Make the File Saving stuff

if __name__ == "__main__":
    main()