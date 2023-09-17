def is_number(random_number, user_guess):
    if user_guess == random_number:
        return True
    return False

def feedback(random_number, user_guess):
    if user_guess > random_number:
        print("Too high!")
    else:
        print("Too low!")

def is_highscore(highscore, score):
    if score < highscore:
        return True
    else:
        return False

def play_again(answer):
    if answer == "Y" or answer == "y":
        return True
    elif answer == "N" or answer == "n":
        return False