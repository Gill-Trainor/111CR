"""
Program: Warehouse Inventory Control System
Functionality:
    - Register Items to the catalog
        id (auto generate)
        title
        category
        price
        stock
    - Display Catalog
    - Display Catalog (items out of stock)
    - Update the stock of a selected item


    - Save Catalog
    - Retrieve Catalog

    **************I need to do Print total value of the current stock (dollar value), using sum = (price * stock), not real code just use this process) *****************

"""

from Menu import print_menu, print_header
from Item import Item
import os
import pickle

catalog = []
id_count = 1
data_file = "catalog.data"

# method declaration


def clear():
    return os.system('cls')

def save_catalog():
    global data_file
    writer = open(data_file, "wb") # open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close()
    print(" Data Saved!!")

def read_catalog():
    global data_file
    global id_count

    try:
        reader = open(data_file, "rb") #open the file to read binary
        temp_list = pickle.load(reader)
        
        for item in temp_list:
            catalog.append(item)

        last = catalog[-1] # get the last element from the array
        id_count = last.id + 1 

        how_many = len(catalog)
        print(" Loaded " + str(how_many) + " Items")
    except:
        # when the code above crashes, we get this
        print(" *Error loading data!")

def register_item():
    global id_count # import the global variable into fn scope
    clear.something = id_count
    print_header('  Register new Item  ')
    title = input('Please input Title: ')
    category = input('Please input Category: ')
    price = float(input('Please input Price: '))
    stock = int(input('Please input Stock '))

    # do validations
    new_item = Item()  # how to create an object of a class
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
   

    id_count += 1
    catalog.append(new_item)
    print("  Item created!")


def display_catalog():
    num_items = len(catalog) # <- get length of array or string
    
    print_header( 'Your Catalog contains '+ str(num_items) +' Items ')
    print('|ID  |   Title              | Category        |     Price | Stock ')
    print('-' * 80)

    for item in catalog:
        if(item.id > 0):
            print("|" + str(item.id).ljust(3) +
                " | " + item.title.ljust(20) 
                + " | " + item.category.ljust(15) 
                + " | " + str(item.price).rjust(9) 
                + " | " + str(item.stock).rjust(5) )

    print('-' * 80)

def display_removed():
    print_header( '  Removed items')
    print(' |   Title              | Category        |     Price | Stock ')
    print('-' * 80)

    for item in catalog:
        if(item.id == 0):
            print(" | " + item.title.ljust(20) 
                + " | " + item.category.ljust(15) 
                + " | " + str(item.price).rjust(9) 
                + " | " + str(item.stock).rjust(5) )

    print('-' * 80)
    

def display_no_stock():
    print_header(' Items left in stock ')
    print('|ID  |   Title              | Category        |     Price | Stock ')
    print('-' * 80)

    for item in catalog:
        print("|" + str(item.id).ljust(3) +
            " | " + item.title.ljust(20) 
            + " | " + item.category.ljust(15) 
            + " | " + str(item.price).rjust(9) 
            + " | " + str(item.stock).rjust(5) )


def update_stock():
    # show all the items
    # ask the user to choose and id
    # ask for the new stock value
    # update the stock value of the selected item
    display_catalog()
    selected = int(input (' please select the ID to update: '))

    found = False
    for item in catalog:
        if(item.id == selected):
            new_stock = input(' Please input new stock value: ')
            item.stock = int(new_stock)
            found = True
            print(' Stock updated!!')

    if(found == False):
        print('** Error: Selected ID does not exist, try again')

def print_stock_value():
    print_header(" Current Stock Value")
    
    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)

        print("Total value: " + str(total))

def remove_item():
      # show all the items
    # ask the user to choose and id to remove
    # validate the id
    # remove that item

    display_catalog()
    selected = int(input (' Please select the ID to remove: '))

    found = False
    for item in catalog:
        if(item.id == selected):
            item.id = 0
            found = True
            print(' Item Removed')

    if(found == False):
        print('** Error: Selected ID does not exist, try again')

def show_removed():
    display_removed()

def list_categories():
    print_header( "List of categories used on the system")
    already_printed = []
    for item in catalog:
        if item.id > 0 and not item.category in already_printed:
            print(item.category)
            already_printed.append(item.category)

# load data
read_catalog()


# loop to display menu
opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Select an option: ')

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        update_stock()
        save_catalog()
    elif(opc == '5'):
        print_stock_value()
    elif(opc == '6'): 
        remove_item()
        save_catalog()
    elif(opc == '7'):
        show_removed()
    elif(opc == '8'):
        list_categories()

    input('Press Enter to continue...')
