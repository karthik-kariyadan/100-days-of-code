from random import choice, shuffle
from string import ascii_letters, digits, punctuation

print("Welcome to the PyPassword Generator!")

letters = int(input("Enter the number of letters you would like in your password: "))
numbers = int(input("Enter the number of numbers you would like in your password: "))
symbols = int(input("Enter the number of symbols you would like in your password: "))

password = []

for _ in range(letters):
    password.append(choice(ascii_letters))

for _ in range(numbers):
    password.append(choice(digits))

for _ in range(symbols):
    password.append(choice(punctuation))

shuffle(password)

print(f"Your password is: {"".join(password)}")
