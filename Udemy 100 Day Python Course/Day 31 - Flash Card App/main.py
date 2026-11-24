from tkinter import Tk, Canvas, PhotoImage, Button


def wrong() -> None:
    print("Wrong")


def right() -> None:
    print("Right")


def flip() -> None:
    print("Flip")


BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
FLIP_FONT = ("Arial", 40, "bold")

window = Tk()
window.focus_force()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
canvas.grid(row=0, column=0, columnspan=3)

card_front = PhotoImage(file="images/card_front.png", width=800, height=526)
canvas.create_image(400, 263, image=card_front)

canvas.create_text(400, 150, text="Title", font=TITLE_FONT, fill="black")
canvas.create_text(400, 263, text="Word", font=WORD_FONT, fill="black")

wrong_button_image = PhotoImage(file="images/wrong.png", width=100, height=99)
wrong_button = Button(image=wrong_button_image, command=wrong, highlightthickness=0, border=0)
wrong_button.grid(row=1, column=0)

flip_button = Button(text="Flip", font=FLIP_FONT, command=flip)
flip_button.grid(row=1, column=1)

right_button_image = PhotoImage(file="images/right.png", width=100, height=100)
right_button = Button(image=right_button_image, command=right, highlightthickness=0, border=0)
right_button.grid(row=1, column=2)

window.mainloop()
