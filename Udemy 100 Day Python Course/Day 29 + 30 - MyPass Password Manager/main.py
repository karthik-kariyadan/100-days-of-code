from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, messagebox
from string import ascii_letters, digits, punctuation
from random import randint, choice, shuffle
from pyperclip import copy
from json import load, dump, decoder


def generate_password() -> str:
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []
    password_list.extend([choice(ascii_letters) for _ in range(nr_letters)])
    password_list.extend([choice(digits) for _ in range(nr_numbers)])
    password_list.extend([choice(punctuation) for _ in range(nr_symbols)])

    shuffle(password_list)

    password = "".join(password_list)

    return password


def create_password() -> None:
    password = generate_password()

    password_entry.delete(0, "end")
    password_entry.insert(0, password)

    copy(password)


def save_data() -> None:
    global website_entry, email_username_entry, password_entry

    try:
        file = open("passwords.json", "r")
        file.close()
    except FileNotFoundError:
        file = open("passwords.json", "w")
        file.close()
    finally:
        with open("passwords.json", "r") as passwords:
            website_text = website_entry.get()
            email_username_text = email_username_entry.get()
            password_text = password_entry.get()
            if website_text and email_username_text and password_text:
                is_ok = messagebox.askokcancel(
                    message=f"Confirm details",
                    detail=f"Website: {website_text}\nEmail/Username: {email_username_text}\nPassword: {password_text}"
                )

                if is_ok:
                    new_data = {
                        website_text: {
                            "email": email_username_text,
                            "password": password_text
                        }
                    }

                    try:
                        data = load(passwords)
                    except decoder.JSONDecodeError:
                        with open("passwords.json", "w") as passwords:
                            dump(new_data, passwords, indent=4)
                    else:
                        with open("passwords.json", "w") as passwords:
                            data.update(new_data)
                            dump(data, passwords, indent=4)
                    finally:
                        website_entry.delete(0, "end")
                        password_entry.delete(0, "end")
            else:
                messagebox.showerror(message="Please do not leave any of the fields empty.")


def search_data() -> None:
    try:
        with open("passwords.json", "r") as passwords:
            data = load(passwords)
    except FileNotFoundError, decoder.JSONDecodeError:
        messagebox.showerror(message="No saved password data found.")
    else:
        website_to_search = website_entry.get()

        try:
            messagebox.showinfo(title=website_to_search,
                                message=f"Email: {data[website_to_search]["email"]}\nPassword: {data[website_to_search]["password"]}")
        except KeyError:
            messagebox.showerror(message="No saved password data found for that website.")


EMAIL = "karthik.kariyadan3@gmail.com"

window = Tk()
window.focus_force()
window.title("MyPass")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, command=search_data)
search_button.grid(row=1, column=2)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

email_username_entry = Entry(width=40)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, EMAIL)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=14, command=create_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=38, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
