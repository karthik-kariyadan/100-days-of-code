from art import *
from random import choice
from word_list import words

word = choice(words)
display = ["_" for _ in word]

lives_art = [lives_0, lives_1, lives_2, lives_3, lives_4, lives_5, lives_6]

print(logo)

lives = 6
guessed_letters = []

while "".join(display) != word and lives != 0:
    print(f"Word to guess: {"".join(display)} ({len(word)} letters)")
    user_guess = input("Guess a letter: ").lower()

    if user_guess not in guessed_letters:
        guessed_letters.append(user_guess)

        if user_guess in word:
            print(f"'{user_guess}' is in the word.")
            for i, char in enumerate(word):
                if char == user_guess:
                    display[i] = char
        else:
            print(f"'{user_guess}' is not in the word. You lose a life.")
            lives -= 1

        print(lives_art[lives])

    else:
        print(f"You have already guessed '{user_guess}'. Enter a different letter.")

if "".join(display) == word:
    print(f"Correct! The word was '{word}'.")
else:
    print(f"You ran out of lives, Game Over! The word was '{word}'.")
