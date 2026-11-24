from data import MENU
from time import sleep


def print_menu() -> None:
    print("\nMENU:")

    for drink in MENU:
        print(f"{drink.title()}: ${MENU[drink]["cost"]:.2f}")


def ask_for_drink() -> str:
    while True:
        user_order = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        if user_order in ["espresso", "latte", "cappuccino", "off", "report"]:
            break
        else:
            print("Please enter a valid drink.")

    if user_order in ["espresso", "latte", "cappuccino"]:
        for resource in resources:
            if MENU[user_order]["ingredients"].get(resource, 0) > resources[resource]:
                print(f"Sorry, there is not enough {resource}.")
                return ""

    return user_order


def check_transaction_successful(money_paid: float | int) -> bool:
    if money_paid > MENU[order]["cost"]:
        change = money_paid - MENU[order]["cost"]
        print(f"Transaction successful. Your change is: ${change:.2f}")
        resources["money"] -= change
        return True

    return False


def process_coins() -> None:
    print("\nINSERT COINS:")

    pennies = int(input("Enter the number of pennies inputted: "))
    nickels = int(input("Enter the number of nickels inputted: "))
    dimes = int(input("Enter the number of dimes inputted: "))
    quarters = int(input("Enter the number of quarters inputted: "))

    money_paid: float | int = pennies * 0.01 + nickels * 0.05 + dimes * 0.1 + quarters * 0.25

    if check_transaction_successful(money_paid):
        resources["money"] += money_paid
        dispense_drink()
    else:
        print(
            f"\nSorry, {order}s cost ${MENU[order]["cost"]:.2f}; you only inputted ${money_paid:.2f}. Money refunded.")


def dispense_drink() -> None:
    print(f"\n{order.title()} is dispensing...")

    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]

    sleep(DISPENSING_TIME)

    print(f"Here is your {order}. Enjoy!")


def print_resources():
    print("\nRESOURCES:")

    for i, resource in enumerate(resources):
        if i < 2:
            print(f"{resource.title()}: {resources[resource]}ml")
        elif i < 3:
            print(f"{resource.title()}: {resources[resource]}g")
        else:
            print(f"{resource.title()}: ${resources[resource]:.2f}")


def shut_down() -> None:
    print("\nCoffee Machine shutting down...")
    sleep(SHUT_DOWN_TIME)
    print("Goodbye!")


DISPENSING_TIME = 3
SHUT_DOWN_TIME = 2

STARTING_WATER = 300
STARTING_MILK = 200
STARTING_COFFEE = 50
STARTING_MONEY = 0

resources: dict[str, float | int] = {
    "water": STARTING_WATER,
    "milk": STARTING_MILK,
    "coffee": STARTING_COFFEE,
    "money": STARTING_MONEY,
}

print_menu()

while True:
    order = ask_for_drink()

    if order == "off":
        break
    elif order == "report":
        print_resources()
    elif order:
        process_coins()

shut_down()
