answer = "Y"

while answer == "Y" or answer == "y":
    print("Enter a positive number lower than 10")

    string_Number = input()
    number = int(string_Number)

    while number >= 10 or number < 0:
        print("This number is invalid!")
        print("Enter a positive number lower than 10")
        string_Number = input()
        number = int(string_Number)

    if number < 9:
        number += 1
        print(str(number) + " I win!")
    elif number == 9:
        print("You win!")

    print("Would you like to play again?")
    answer = input()

print("Thanks for playing!")
