# And Import Statement to make code from other files available
from models.item import Item
import csv
import tempfile
import shutil

next_id = 0
items = []  # This will be used to store items

def menu():  # Prints Menu Options for the user
    print("""
    1. List All Items
    2. Add New Item
    3. Update Existing Item
    4. Delete Item (By item id)
    5. Exit
    """)


def list_items():  # Writes all items to the Terminal
    """
    1.) Read file into python
    2.) Parse the file into usable data
    3.)Print out each item in the file
    """

    with open('inventory.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            message = f"ID: { row['id'] }\tName: { row['name'] }\tCondition: { row['condition']}"
            print(message)

    # for item in items:
    #     print(item)

def new_item():  # Gets user input for all need fields for an Item
    """
    1.) open and parse the file into CSV
    2.) detect what the next id will be
    3.)promt the user for new item data (name, condition)
    4.) add this item to the inventory.csv file
    """
    with open('inventory.csv', 'r+') as file:
        current_items = list(csv.DictReader(file))
        try:
            last_id = int(current_items[-1]['id'])
        except IndexError:
            last_id = -1
    with open('inventory.csv', 'a+', newline="") as file:
        name = input('Name: > ')
        condition = input('Condition: > ')
        item ={
            "id": last_id + 1,
            "name": name,
            "condition": condition
        }
        writer = csv.DictWriter(file, ["id", "name", "condition"], )
        if last_id ==-1:
            writer.writeheader()
        writer.writerow(item)


def update_existing():  # Update Existing Item
    """
    TODO
    1.) Ask the user which of the existing items to update. 
    2.)Display the item ask to verify if it is the correct item for update
    3.)Ask what values to update
    4.) create a temporary file in python, which is a copy of the csv (tempfile)
    5.) line by line, copy the information over to the new temp file
    6.)when we reach the item we want ot update, then write the new line (changed data)
    7.) continue line by line until the file is complete
    8.) overwrite the old csv file. (shutil)
    """

    with open('inventory.csv', 'r') as file:
        reader = csv.DictReader(file)
        if len(list(reader)) == 0:
            print('No items for you to update. Exiting update...')
            return
        else:
            # Go back to the beginning of the file, and skip the header line
            file.seek(0)
            file.readline()
        choice = input('Which item to update, choose an ID: > ')
        # TODO: Check if the item exists
        new_name = input('Change for the name (blank to leave as is): > ')
        new_condition = input('Change for the condition (blank to leave as is): > ')
        temp_file = tempfile.NamedTemporaryFile(mode='w', newline='', delete=False)
        csv_writer = csv.DictWriter(temp_file, ['id', 'name', 'condition'])
        csv_writer.writeheader()
        for item in reader:
            print(item)
            if item['id'] == choice:
                updated_item = {
                    'id': item['id'],
                    'name': new_name if len(new_name) > 0 else item['name'],
                    'condition': new_condition if len(new_condition) > 0 else item['condition']
                }
                csv_writer.writerow(updated_item)
            else:
                csv_writer.writerow(item)
        temp_file.close()
    shutil.move(temp_file.name, 'inventory.csv')


# Delete Item (By item id)
def delete_item():
    if not items:
        print("You have no items to delete")
        return
    list_items()
    try:
        item_id_to_delete = int(input("What is the item id you wish to update\n> "))
    except Exception:
        print("Not a valid number.")
        return

    for index, item in enumerate(items):
        if item.item_id == item_id_to_delete:
            index_to_remove = index
            break
    else:
        print("We didn't find a match")
        return
    removed_item = items.pop(index_to_remove)
    print(f"Found:\n{removed_item} it has been removed")


def main():  # Starts the Program off, holds the loop until exit.
    # Detect if hte inventory.scv file exists. Create if no. 
    open('inventory.csv', 'a+').close()
    while True:
        menu()  # Prints the Options to the Terminal
        choice = input("> ")  # Takes use choice

        # The Conditional Options: hands off the work to the functions above.
        if choice == "1":
            list_items()
        elif choice == "2":
            new_item()
        elif choice == "3":
            update_existing()
        elif choice == "4":
            delete_item()

        elif choice == "5":  # Exit
            exit()
        else:  # User gave us bad input we let them know then loop again.
            input("Invalid Input!\n(Press Enter to try again)")


# TODO Make the File Saving stuff

if __name__ == "__main__":
    main()