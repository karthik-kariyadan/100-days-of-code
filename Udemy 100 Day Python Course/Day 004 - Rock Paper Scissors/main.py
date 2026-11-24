from art import rock, paper, scissors
from random import randint

images = [rock, paper, scissors]

user_choice = int(input("Enter your choice (0 = Rock, 1 = Paper, 2 = Scissors): "))

if 0 <= user_choice <=2:
    print(images[user_choice])
else:
    print("Invalid choice.")

computer_choice = randint(0, 2)

print("Computer chose: ")

print(images[computer_choice])

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0:
    if computer_choice == 1:
        print("You lose.")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win!")
    else:
        print("You lose!")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose!")
    else:
        print("You win!")
