with open("art.txt", "r") as art:
    chest = art.read()

print(chest)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")

cross_road = input("\tType 'left' or 'right'\n").lower()

if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")

    lake = input("\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    if lake == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")

        colour = input("\tOne 'red', one 'yellow' and one 'blue'. Which colour do you choose?\n").lower()

        if colour == "red":
            print("It's a room full of fire. Game Over.")
        elif colour == "yellow":
            print("You found the treasure! You Win!")
        elif colour == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Invalid answer. Game Over.")
    elif lake == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid answer. Game Over.")
elif cross_road == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Invalid answer. Game Over.")
