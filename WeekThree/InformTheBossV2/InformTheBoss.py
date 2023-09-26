from my_functions import store_functions

while True:
	store_functions.get_options()
	user_input = input("> ")

	if user_input == "s" or user_input == "S":
		name = input("Name: ")
		if name in store_functions.get_list_items():
			quantity = int(input("Quantity:  "))
			store_functions.add_item(name, 0, quantity)
		else :
			price = float(input("Price: "))
			quantity = int(input("Quantity:  "))
			store_functions.add_item(name, price, quantity)
	elif user_input == "i" or user_input == "I":
		if len(store_functions.get_list_items()) == 0:
			print("There has not yet been any sales.")
		else:
			print("All items sold:")
			for item in store_functions.get_list_items():
				print(item, end=" ")
			print("")
			print("Total sales:")
			print(store_functions.get_total_sales())
	elif user_input == "exit" or user_input == "Exit":
		break
	else:
		print(f"Sorry, the command ({user_input}) is unrecognised.")