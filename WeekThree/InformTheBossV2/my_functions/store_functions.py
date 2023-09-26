store_inventory = {}
total_sale = 0


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

def get_total_sales():
	total_sale = 0
	for item in store_inventory :
		total_sale += float(store_inventory[item]["price"] * store_inventory[item]["quantity"])
	return total_sale

def get_list_items() :
	list_items = []
	for item in store_inventory :
		list_items.append(store_inventory[item]["name"])
	return list_items

def get_options() :
	print("")
	print("What would you like to do?")
	print("S = New sale.")
	print("I = Display sale information.")
	print("Exit = Exit the program.")
