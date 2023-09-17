import random

random_number = random.randint(1, 100)
answer = None

while answer != random_number:
    print("Guess a number between 1 and 100")
    answer = int(input(">"))

    if answer == random_number:
        print("")
        break
    elif answer < 1 or answer > 100:
        print("This number is invalid!")
        print("")
    elif answer > random_number:
        print("Too high!")
        print("")
    else:
        print("Too low!")
        print("")

print(f"Congratulations! You guessed the right number ({random_number})")
