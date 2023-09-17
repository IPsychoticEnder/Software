import random
from MyFunctions import GameFunctions

random_number = None
answer = "Y"
score = 0
highscore = float("inf")

while GameFunctions.play_again(answer):
    random_number = random.randint(1, 100)
    print(random_number)

    while True:
        print("")
        print("Guess a number between 1 and 100")
        user_guess = int(input(">"))

        if GameFunctions.is_number(random_number, user_guess):
            print("You win!")
            print("")
            break
        else:
            GameFunctions.feedback(random_number, user_guess)
            score += 1

    if GameFunctions.is_highscore(highscore, score):
        print(f"You have a new high score! ({score})")
        score = 0
    
    print("Would you like to play again? (Y/N)")
    answer = input(">")
