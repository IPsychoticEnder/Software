while True:
    print("Please enter a valid year: ")
    user_input = input()

    while int(user_input) < 0:
        print("This is not a valid year, Please enter a valid year.")
        user_input = input()

    year = int(user_input)

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("This year is a leap year.")
    else:
        print("This year is not a leap year.")
