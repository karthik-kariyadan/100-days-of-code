from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep
from tkinter import Button


def check_for_collision_with_food() -> None:
    global sleep_time

    if snake.head.distance(food) < 15:
        food.refresh(snake.segments)
        snake.add_segment((snake.segments[-1].position()[0], snake.segments[-1].position()[1]))
        scoreboard.increase_score()
        sleep_time *= 0.98


def colling_with_wall() -> bool:
    if snake.head.xcor() <= -300 or snake.head.xcor() >= 300 or snake.head.ycor() <= -300 or snake.head.ycor() >= 300:
        return True

    return False


def colliding_with_tail() -> bool:
    for segment in snake.segments:
        if snake.head.distance(segment) < 15 and segment != snake.head:
            return True

    return False


def retry() -> None:
    global running, sleep_time

    sleep_time = STARTING_SLEEP_TIME

    scoreboard.reset()
    snake.reset()
    game_over_button.destroy()
    food.refresh(snake.segments)

    running = True


def game_over():
    global running, game_over_button
    scoreboard.game_over()
    running = False

    game_over_button = Button(
        screen.getcanvas().master,
        text="RETRY",
        command=retry,
        font=("ArcadeClassic", 50, "bold")
    )

    game_over_button.pack()
    game_over_button.place(x=220, y=300)


STARTING_SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

root = screen.getcanvas().winfo_toplevel()
root.attributes("-topmost", True)
root.lift()
root.focus_force()
root.after(100, lambda *args: root.attributes("-topmost", False), None)

snake: Snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(retry, "r")

food: Food = Food(snake.segments)
scoreboard: Scoreboard = Scoreboard()

sleep_time = STARTING_SLEEP_TIME

game_over_button: Button = Button()

running: bool = True

while True:
    screen.update()
    sleep(sleep_time)

    if running:
        snake.move()

        check_for_collision_with_food()

        if colling_with_wall() or colliding_with_tail():
            game_over()
