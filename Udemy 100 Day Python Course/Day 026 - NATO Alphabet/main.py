from pandas import DataFrame, read_csv
from string import ascii_uppercase

user_text = input("Enter the text you would like to convert to the NATO Phonetic Alphabet: ").upper()

print("\n".join(
    ", ".join([
        DataFrame(read_csv("nato_phonetic_alphabet.csv")).code[
            DataFrame(read_csv("nato_phonetic_alphabet.csv")).letter == char
            ].to_list()[0]
        for char in user_text.split(" ")[i]
        if char in ascii_uppercase
    ])
    for i in range(len(user_text.split(" ")))
))
