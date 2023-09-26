from my_functions import store_functions

while True :
    store_functions.get_options()
    user_input = input("> ")
    if user_input == "s" or user_input == "S":
        name = input("name: ")
        price = float(input("price: "))
        quantity = int(input("quantity: "))
        store_functions.add_item(name, price, quantity)

    elif user_input == "i" or user_input == "I":
        print("What information would you like? ")
        store_functions.get_sold_items_list()
        store_functions.get_total_sale()
        user_input = input("> ")

    elif user_input == "exit" or user_input == "Exit":
        break
    else :
        print("Try again")