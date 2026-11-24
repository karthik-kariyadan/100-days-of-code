with open("./Input/Letters/starting_letter.txt", "r") as starting_letter_file:
    starting_letter = starting_letter_file.read()

with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    invited_names = [name.strip("\n") for name in invited_names_file.readlines()]

for name in invited_names:
    with open(f"./Output/Ready To Send/LetterFor{name.replace(" ", "")}", "w") as new_letter:
        new_letter.write(starting_letter.replace("[name]", name))
