from tkinter import Tk, Canvas, PhotoImage, Label, Button


def start_timer() -> None:
    global reps, timer_label, ticks

    reps += 1
    reps %= 8

    if reps % 2 == 0:
        ticks.config(text=ticks.cget("text") + "✔")

        if reps == 0:
            timer_label.config(text="Long Break", fg=RED)
            countdown(LONG_BREAK_MIN * 60)
        else:
            timer_label.config(text="Short Break", fg=PINK)
            countdown(SHORT_BREAK_MIN * 60)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


def reset_timer() -> None:
    global window, timer, canvas, timer_text, timer_label, reps, ticks

    reps = 0
    window.after_cancel(timer)

    timer_label.config(text="Timer", fg=GREEN)
    ticks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


def countdown(count: float | int) -> None:
    global canvas, timer_text, window, timer

    minutes = f"{int(count // 60):02}"
    seconds = f"{int(count % 60):02}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        window.focus_force()


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = ""

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.focus_force()

tomato = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
canvas.grid(row=1, column=1, padx=75)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

ticks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "normal"))
ticks.grid(row=3, column=1)

window.mainloop()
