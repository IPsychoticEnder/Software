sold_flowers = {}
highest_sale = float(0)
highest_sale_name = ""
lowest_sale = float("inf")
lowest_sale_name = ""
average_sale = 0
total_sale = float(0)

# Create a while loop to keep the program going untill the user types "Exit"
while True:
    # Asks the user what he would like to do and give the available options
    print("What would you like to do?")
    print("S = New sale.")
    print("I = Give total sale information.")
    print("Exit = Exit the program.")
    command = input(">")
    print("")

    if command == "S":
        # Asks the user to input the name and the price of the item, then converts the price to a float.
        # Sums up the total sale of all the items.
        flower_name = input("Name: ")
        flower_price = float(input("Price: "))
        total_sale += flower_price
        # Adds the givven input to the dictionary
        sold_flowers[flower_name] = flower_price
        print("")
    elif command == "I":
        if len(sold_flowers) == 0:
            print("There has not been any sales yet.")
            print("")
        else:
            total_flowers_sold = len(sold_flowers)

            for flower_name, flower_price in sold_flowers.items():
                if flower_price > highest_sale:
                    highest_sale_name = flower_name
                    highest_sale = flower_price

                if flower_price < lowest_sale:
                    lowest_sale_name = flower_name
                    lowest_sale = flower_price

            average_sale = round((total_sale / total_flowers_sold), 2)

            print(f"There has been {total_flowers_sold} flowers sold.")
            print(
                f"The most expensive sale is {highest_sale_name} valued at {highest_sale} Euro."
            )
            print(
                f"The least expensive sale is {lowest_sale_name} valued at {lowest_sale} Euro."
            )
            print(f"The average sale is {average_sale} Euro.")
            print("")
    elif command == "Exit":
        break
    else:
        print(f"Sorry, this command ({command}) is invalid!")
        print("")
