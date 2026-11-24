from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable


def print_menu() -> None:
    table: PrettyTable = PrettyTable()

    table.add_column("Drink", ["Espresso", "Latte", "Cappuccino"])
    table.add_column("Price", ["$1.50", "$2.50", "$3.00"])

    table.align = "l"

    print(table)


def ask_for_drink() -> str:
    while True:
        user_order: str = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()

        if user_order in ["espresso", "latte", "cappuccino", "report", "off"]:
            break
        else:
            print("Please enter a valid drink.")

    return user_order


menu: Menu = Menu()
coffee_maker: CoffeeMaker = CoffeeMaker()
money_machine: MoneyMachine = MoneyMachine()

print_menu()

while True:
    order: str = ask_for_drink()

    if order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order: MenuItem = menu.find_drink(order)

        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
