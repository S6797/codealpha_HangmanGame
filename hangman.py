
import random

words = ["apple", "mango", "python", "school", "computer"]

word = random.choice(words)
guessed = ""
chance = 6

print("Welcome to Hangman Game!")

while chance > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)
    print("Chances left:", chance)

    if display == word:
        print("You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("Already guessed!")
    elif guess in word:
        guessed += guess
        print("Correct guess!")
    else:
        chance -= 1
        guessed += guess
        print("Wrong guess!")

if chance == 0:
    print("You Lose!")
    print("Correct word was:", word)
