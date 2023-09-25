store_inventory = {}

def get_options() :
    print("")
    print("What would you like to do?")
    print("S = New sale.")
    print("I = Display sale information.")
    print("Exit = Exit the program.")

def add_item(name, price, quantity) :
    item_details = {
        "name": name,
        "price": price,
        "quantity": quantity,
    }
    if name in store_inventory :
        store_inventory[name]["quantity"] += quantity
    else :
        store_inventory[name] = item_details

def get_store_info(name) :
    print(store_inventory[name])