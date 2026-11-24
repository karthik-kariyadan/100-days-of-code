from art import logo
from subprocess import run

names: dict[str, float | int] = {}
more_bidders = "yes"

while more_bidders == "yes":
    print(logo)

    name: str = input("Enter your name: ")
    bid: float | int = float(input("Enter your bid: £"))

    while True:
        more_bidders = input("Enter 'yes' if there are more bidders, otherwise type 'no': ").lower()

        if more_bidders not in ["yes", "no"]:
            print("Please type a valid answer.")
        else:
            break

    names[name] = bid
    run("clear")

    if more_bidders == "no":
        break

winning_bid = max(names.values())
winner = list(names.keys())[list(names.values()).index(winning_bid)]

print(logo)
print(f"The winner is {winner} with a bid of: £{winning_bid:.2f}")
