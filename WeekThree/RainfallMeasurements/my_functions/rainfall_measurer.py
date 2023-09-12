sum = 0
average = None
user_input = None
rainfall = list()


def create_rainfall_list():
    global rainfall
    global user_input

    while user_input != "":
        print("")
        print("Please enter the ammount of rainfall:")
        print("Empty to stop.")
        user_input = input("> ")
        if user_input != "":
            rainfall.append(float(user_input))
    return rainfall


def get_sum(list):
    global sum

    for i in range(len(list)):
        sum += list[i]

    return sum


def get_average(list):
    global sum
    global average

    average = sum / len(list)
    return average


def print_rain_info():
    global rainfall
    global sum
    global average

    print("Rainfall: ", end="")
    for i in range(len(rainfall)):
        print(f"{rainfall[i]}", end="")
        if i + 1 < len(rainfall):
            print(" - ", end="")
    print("")
    print(f"Total rainfall: {sum}")
    print(f"Average rainfall: {average}")
