from art import logo
from random import randint

print(logo, "\nWelcome to the Guess The Number!\nI'm thinking of a number between 1 and 100 (inclusive).")

while True:
    difficulty = input("Enter the difficulty: (easy/hard): ").lower()

    if difficulty in ["easy", "hard"]:
        break
    else:
        print("Please enter a valid difficulty.")

if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

answer = randint(1, 100)
user_guess = 0

while user_guess != answer:
    while True:
        user_guess = int(input("Enter your guess as a number between 1 and 100 inclusive: "))

        if 1 <= user_guess <= 100:
            user_guess = int(user_guess)
            break
        else:
            print("Please enter a valid guess.")

    if user_guess > answer:
        print(f"Too high, you have {guesses} guesses remaining.")
    elif user_guess < answer:
        print(f"Too low, you have {guesses} guesses remaining.")
    else:
        print(f"You win! The number was: {answer}.")
        break

    guesses -= 1

    if guesses == 0:
        print(f"You ran out of guesses! The number was: {answer}.")
        break
