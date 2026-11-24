from turtle import Turtle, Screen
from random import random


def create_turtles() -> None:
    screen.tracer(0)

    for i, color in enumerate(COLORS):
        turtle = Turtle(shape="turtle")
        turtle.turtlesize(TURTLE_STRETCH_X, TURTLE_STRETCH_Y)
        turtle.color(color)
        turtle.speed(0)
        turtle.penup()
        turtle.goto(TURTLE_STARTING_X, TURTLE_SPACING * i - TURTLE_OFFSET)
        turtles.append(turtle)

    screen.tracer(60)


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BG_COLOR = "light green"

TURTLE_STRETCH_X = 2
TURTLE_STRETCH_Y = 2
TURTLE_STARTING_X = -325
TURTLE_SPACING = 100
TURTLE_OFFSET = 250
TURTLE_MOVEMENT = 1
TURTLE_WINNING_X = 327

screen = Screen()
screen.bgcolor(BG_COLOR)

turtles = []
create_turtles()

user_bet = str(screen.textinput(
    "Make your bet",
    f"Who do you think will win the race?\nThe colors are: {', '.join(color.title() for color in COLORS)}."
)).lower()

winner: Turtle = Turtle()
winner.hideturtle()

while winner.color()[0] == "black":
    for turtle in turtles:
        turtle.forward(TURTLE_MOVEMENT if random() > 0.95 else 0)

    for turtle in turtles:
        if turtle.xcor() >= TURTLE_WINNING_X:
            winner: Turtle = turtle
            break

if user_bet == winner.color()[0].lower():
    print(f"You win! The winner was: {winner.color()[0].title()}.")
else:
    print(f"You lose! The winner was: {winner.color()[0].title()}.")

screen.exitonclick()
