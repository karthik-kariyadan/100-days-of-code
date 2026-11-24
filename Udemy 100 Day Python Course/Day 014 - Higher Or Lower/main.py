from game_data import data
from art import logo, vs
from random import choice
from subprocess import run

print(logo)
score = 0
a = {}
b = choice(data)

while True:
    a = b
    b = choice(data)

    while a == b:
        b = choice(data)

    answer = "a" if a["follower_count"] > b["follower_count"] else "b"

    print(f"Compare A: {a["name"]}, a {a["description"]} from {a["country"]}.")
    print(vs)
    print(f"Against B: {b["name"]}, a {b["description"]} from {b["country"]}.")

    while True:
        user_guess = input("Who has more followers on Instagram? Type 'A' or 'B': ").lower()

        if user_guess in ["a", "b"]:
            break
        else:
            print("Please enter a valid guess.\n")

    if user_guess == answer:
        score += 1
        run("clear")
        print(logo, f"\nYou're right! Current score: {score}.")
    else:
        run("clear")
        print(logo, f"\nSorry, that's wrong. Final score: {score}.")
        break
