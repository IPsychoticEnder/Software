word = "elephant"
secret_word = list(word)
starred_hidden_word = list()

print("")
print("")
print("Welcome to HangMan")
print("")
print(f"The word you have to guess consists of {len(secret_word)} characters.")

for letter in secret_word:
    starred_hidden_word.append("*")

while "*" in starred_hidden_word:
    print("Please guess a letter in the word:")
    for star in starred_hidden_word:
        print(f"{star} ", end="")
    print("")
    guess = input(">")
    print("")

    if guess in secret_word:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                starred_hidden_word[i] = guess
        if "*" in starred_hidden_word:
            print("Congratulations! You guessed one of the letters right!")
    else:
        print("The letter you guessed is not in the word.")


print(f"Congratulations, you guessed {word.capitalize()} completely!")
