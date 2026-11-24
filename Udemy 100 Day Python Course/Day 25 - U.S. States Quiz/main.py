from turtle import Turtle, Screen, shape
from pandas import DataFrame, read_csv


def force_screen_front() -> None:
    global root

    root = screen.getcanvas().winfo_toplevel()
    root.attributes("-topmost", True)
    root.lift()
    root.focus_force()
    root.after(0, lambda *args: root.attributes("-topmost", False), None)


NUM_OF_STATES = 50

screen = Screen()
screen.title("U.S. States Game")

root = ...
force_screen_front()

blank_states = "blank_states.gif"
screen.addshape(blank_states)
shape(blank_states)

# noinspection PyArgumentList
states = DataFrame(read_csv("50_states.csv"))

guessed_states: list[str] = []

num_of_correct_states = 0
correct_or_incorrect = ""

while num_of_correct_states < NUM_OF_STATES:
    answer_state = str(screen.textinput(
        title=f"{num_of_correct_states}/{NUM_OF_STATES} States Correct",
        prompt=f"{correct_or_incorrect}Enter the name of a state, or type 'give up' to show missed states."
    )).title()

    if answer_state == "Give Up":
        DataFrame(state for state in states.state.to_list() if state not in guessed_states).to_csv("missed_states.csv")
        break
    elif answer_state in guessed_states:
        correct_or_incorrect = "Already guessed. "
    elif answer_state in states.state.to_list():
        num_of_correct_states += 1
        correct_or_incorrect = "Correct! "
        guessed_states.append(answer_state)

        state_data = states[states.state == answer_state]

        text = Turtle()

        text.hideturtle()
        text.penup()
        text.speed(0)
        text.goto(int(state_data.x.to_list()[0]), int(state_data.y.to_list()[0]))

        text.write(state_data.state.to_list()[0], False, "center", ("Courier", 10, "normal"))
    else:
        correct_or_incorrect = "Incorrect. "

screen.exitonclick()
