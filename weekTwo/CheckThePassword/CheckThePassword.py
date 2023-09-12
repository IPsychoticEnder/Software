password = "Banana"
i = 1

userInput = input("Password: ")

while userInput != password:
    print("Your password is incorrect!")
    attempts_remaining = f"{3 - i} attempts remaining"
    print(attempts_remaining)
    userInput = input("Password: ")
    i += 1
    if i == 3:
        print("Your account has been blocked!")
        break

if userInput == password:
    print("Your password is correct!")
