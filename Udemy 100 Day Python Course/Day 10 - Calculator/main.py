from art import logo
from subprocess import run

while True:
    print(logo)
    num1: float | int = float(input("Enter the first number: "))

    while True:
        operation: str = input("Enter the operation (+, -, *, or /): ")
        num2: float | int = float(input("Enter the second number: "))

        if operation in ["+", "-", "*", "/"]:
            answer = eval(f"{num1} {operation} {num2}")
            print(f"{num1} {operation} {num2} = {answer}")

            while True:
                will_continue = input(
                    f"Type 'yes' to continue calculating with {answer}, or type 'no' to start a new calculation: "
                ).lower()

                if will_continue in ["yes", "no"]:
                    break
                else:
                    print("Please type a valid answer.")

            if will_continue == "no":
                run("clear")
                break
            else:
                num1 = answer
        else:
            print("Equation invalid.")
