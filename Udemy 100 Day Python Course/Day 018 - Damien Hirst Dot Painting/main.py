from turtle import Turtle, Screen
from colors import COLORS

NUM_OF_COLORS = 180
LENGTH = 6
WIDTH = 5
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
DOT_SiZE = 30
TURTLE_X = -150
TURTLE_Y = 185
TURTLE_MOVEMENT = 75

turtle = Turtle()
screen = Screen()

turtle.shape("turtle")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(TURTLE_X, TURTLE_Y)

screen.colormode(255)
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

for i in range(LENGTH):
    for j in range(WIDTH):
        turtle.color(COLORS[i * WIDTH + j])
        turtle.pendown()
        turtle.dot(DOT_SiZE)
        turtle.penup()
        turtle.forward(TURTLE_MOVEMENT)

    turtle.setx(TURTLE_X)
    turtle.right(90)
    turtle.forward(TURTLE_MOVEMENT)
    turtle.right(270)

screen.exitonclick()
