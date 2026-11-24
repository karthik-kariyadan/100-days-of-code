from art import logo
from string import ascii_lowercase

def caesar(shift_mode: str, original_message: str, shift_number: int) -> str:
    if shift_mode == "decode":
        shift_number *= -1

    ciphered_message = ""
    for char in original_message:
        if char in alphabet:
            ciphered_message += alphabet[alphabet.index(char) + shift_number]
        else:
            ciphered_message += char

    return ciphered_message

alphabet = list(ascii_lowercase * 2)

print(logo)

while True:
    while True:
        mode = input("Type 'encode' to encrypt, or 'decode' to decrypt: ").lower()

        if mode not in ["encode", "decode"]:
            print("Please type a valid mode.")
        else:
            break

    message = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))

    print(f"Your {mode}d message is: {caesar(mode, message, shift % 26)}.")

    while True:
        will_continue = input("Type 'yes' to continue, or 'no' to quit: ")

        if will_continue in ["yes", "no"]:
            break
        else:
            print("Please type a valid answer.")

    if will_continue == "no":
        break
