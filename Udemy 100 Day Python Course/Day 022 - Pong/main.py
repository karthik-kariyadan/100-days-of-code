from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from turtle import Screen
from time import sleep

BALL_MAXIMUM_DISTANCE = 290

BALL_SPEED_INCREASE = 1.05
PADDLE_STRETCH_WIDTH_DECREASE = 0.975
PADDLE_MAXIMUM_DISTANCE_OFFSET = 10


def setup_screen():
    screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)


def force_screen_on_top():
    global root
    root = screen.getcanvas().winfo_toplevel()
    root.attributes("-topmost", True)
    root.lift()
    root.focus_force()
    root.after(100, lambda *args: root.attributes("-topmost", False), None)


def start_moving_left_paddle_up() -> None:
    global left_paddle_moving_up
    left_paddle_moving_up = True


def stop_moving_left_paddle_up() -> None:
    global left_paddle_moving_up
    left_paddle_moving_up = False


def start_moving_left_paddle_down() -> None:
    global left_paddle_moving_down
    left_paddle_moving_down = True


def stop_moving_left_paddle_down() -> None:
    global left_paddle_moving_down
    left_paddle_moving_down = False


def start_moving_right_paddle_up() -> None:
    global right_paddle_moving_up
    right_paddle_moving_up = True


def stop_moving_right_paddle_up() -> None:
    global right_paddle_moving_up
    right_paddle_moving_up = False


def start_moving_right_paddle_down() -> None:
    global right_paddle_moving_down
    right_paddle_moving_down = True


def stop_moving_right_paddle_down() -> None:
    global right_paddle_moving_down
    right_paddle_moving_down = False


def check_for_key_presses():
    screen.onkeypress(start_moving_left_paddle_up, "w")
    screen.onkeyrelease(stop_moving_left_paddle_up, "w")

    screen.onkeypress(start_moving_left_paddle_down, "s")
    screen.onkeyrelease(stop_moving_left_paddle_down, "s")

    screen.onkeypress(start_moving_right_paddle_up, "Up")
    screen.onkeyrelease(stop_moving_right_paddle_up, "Up")

    screen.onkeypress(start_moving_right_paddle_down, "Down")
    screen.onkeyrelease(stop_moving_right_paddle_down, "Down")

    screen.onkeypress(start_moving_right_paddle_up, "i")
    screen.onkeyrelease(stop_moving_right_paddle_up, "i")

    screen.onkeypress(start_moving_right_paddle_down, "k")
    screen.onkeyrelease(stop_moving_right_paddle_down, "k")


def check_for_left_paddle_movement():
    if left_paddle_moving_up:
        paddle_left.up()
    elif left_paddle_moving_down:
        paddle_left.down()


def check_for_right_paddle_movement():
    if right_paddle_moving_up:
        paddle_right.up()
    elif right_paddle_moving_down:
        paddle_right.down()


def increase_difficulty() -> None:
    ball.ball_speed *= BALL_SPEED_INCREASE

    paddle_left.stretch_width *= PADDLE_STRETCH_WIDTH_DECREASE
    paddle_right.stretch_width *= PADDLE_STRETCH_WIDTH_DECREASE

    paddle_left.shapesize(stretch_len=paddle_left.stretch_length, stretch_wid=paddle_left.stretch_width)
    paddle_right.shapesize(stretch_len=paddle_right.stretch_length, stretch_wid=paddle_right.stretch_width)

    paddle_left.maximum_distance = paddle_left.starting_maximum_distance + (
            PADDLE_MAXIMUM_DISTANCE_OFFSET / paddle_left.stretch_width)
    paddle_right.maximum_distance = paddle_right.starting_maximum_distance + (
            PADDLE_MAXIMUM_DISTANCE_OFFSET / paddle_right.stretch_width)


def check_for_ball_collisions():
    if ball.check_collision_with_wall():
        ball.bounce_wall()
    elif ball.check_collision_with_paddle(paddle_left):
        ball.bounce_paddle(paddle_left)
        increase_difficulty()
    elif ball.check_collision_with_paddle(paddle_right):
        ball.bounce_paddle(paddle_right)
        increase_difficulty()


def restart() -> None:
    scoreboard.draw_score()
    ball.home()
    paddle_left.goto(-1 * paddle_left.starting_x, 0)
    paddle_right.goto(paddle_right.starting_x, 0)
    ball.initialise_speed_and_direction()
    paddle_left.initialise_stretch_width_and_maximum_distance()
    paddle_right.initialise_stretch_width_and_maximum_distance()
    screen.update()
    sleep(2)


def check_for_win() -> None:
    if ball.xcor() <= (-1 * BALL_MAXIMUM_DISTANCE):
        scoreboard.right_score += 1
        restart()
    elif ball.xcor() >= BALL_MAXIMUM_DISTANCE:
        scoreboard.left_score += 1
        restart()


SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

STARTING_SLEEP_TIME = 0.01

screen = Screen()

setup_screen()

root = ""

force_screen_on_top()

paddle_left = Paddle("left")
paddle_right = Paddle("right")

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

check_for_key_presses()

left_paddle_moving_up: bool = False
left_paddle_moving_down: bool = False
right_paddle_moving_up: bool = False
right_paddle_moving_down: bool = False

sleep_time = STARTING_SLEEP_TIME

scoreboard.draw_score()
screen.update()
sleep(2)

while True:
    screen.update()
    scoreboard.draw_score()
    sleep(sleep_time)

    check_for_left_paddle_movement()
    check_for_right_paddle_movement()
    check_for_ball_collisions()
    check_for_win()

    ball.move()
