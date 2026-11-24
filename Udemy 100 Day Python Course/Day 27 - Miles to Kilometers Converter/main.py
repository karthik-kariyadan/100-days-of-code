from tkinter import Tk, Label, Button, Entry, END


def force_screen_focus() -> None:
    window.attributes("-topmost", True)
    window.lift()
    window.focus_force()
    window.after(0, lambda *args: window.attributes("-topmost", False), None)


def center_window() -> None:
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def calculate(event=None) -> None:
    kilometers.config(text=str(round(float(miles.get()) * 1.60934, 3)))
    miles.delete(0, END)


FONT = ("Calibri", 20, "normal")

window = Tk()

window.title("Unit Converter")
window.minsize(width=100, height=100)
window.config(padx=50, pady=50)

miles = Entry(width=5)
miles.grid(row=0, column=1)

miles_label = Label(text="miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)

kilometers = Label(text="0", font=FONT)
kilometers.grid(row=1, column=1)

kilometers_label = Label(text="kilometers", font=FONT)
kilometers_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.bind("<Return>", calculate)

force_screen_focus()
center_window()

miles.focus()

window.mainloop()
