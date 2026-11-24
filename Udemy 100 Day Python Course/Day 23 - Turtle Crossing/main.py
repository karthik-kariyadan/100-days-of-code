from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

from turtle import Screen
from time import sleep
from random import randint

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

DELTA_TIME = 0.1
STARTING_NUMBER_OF_CARS_PER_SECOND = 2

WINNING_Y_COR = 280


def setup_screen() -> None:
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgcolor("pale green")
    screen.tracer(0)

    force_screen_focus()


def force_screen_focus() -> None:
    global root
    root = screen.getcanvas().winfo_toplevel()
    root.attributes("-topmost", True)
    root.lift()
    root.focus_force()
    root.after(0, lambda *args: root.attributes("-topmost", False), None)


def move() -> None:
    global player_moving

    player_moving = True


def stop_move() -> None:
    global player_moving

    player_moving = False


def next_level():
    global num_of_starting_cars_to_spawn
    global number_of_cars_per_second

    player.next_level()

    for car_object in car_manager.cars:
        car_object.hideturtle()

    car_manager.cars = []

    number_of_cars_per_second *= 2

    num_of_starting_cars_to_spawn = int(
        number_of_cars_per_second * (SCREEN_WIDTH / car_manager.move_increment) * DELTA_TIME
    )
    car_manager.spawn_starting_cars(num_of_starting_cars_to_spawn)

    car_manager.move_increment *= 2

    scoreboard.level += 1
    scoreboard.write_level()


screen = Screen()
root = ""

setup_screen()

screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(move, "w")
screen.onkeypress(move, "i")
screen.onkeypress(move, "Up")
screen.onkeypress(move, "space")

screen.onkeyrelease(stop_move, "w")
screen.onkeyrelease(stop_move, "i")
screen.onkeyrelease(stop_move, "Up")
screen.onkeyrelease(stop_move, "space")

running = True
time: float | int = 0
number_of_cars_per_second = STARTING_NUMBER_OF_CARS_PER_SECOND

num_of_starting_cars_to_spawn = int(
    number_of_cars_per_second * (SCREEN_WIDTH / car_manager.move_increment) * DELTA_TIME
)
car_manager.spawn_starting_cars(num_of_starting_cars_to_spawn)

scoreboard.write_level()

player_moving = False

while running:
    sleep(DELTA_TIME)
    time += DELTA_TIME

    if player_moving:
        player.move()

    should_spawn_new_car = round(round(time, 1) % (1 / number_of_cars_per_second), 1)

    if should_spawn_new_car == 0 or should_spawn_new_car == (1 / number_of_cars_per_second):
        car_manager.spawn_new_car((
            car_manager.car_spawn_x,
            randint(int(car_manager.minimum_car_spawn_y / 25), int(car_manager.maximum_car_spawn_y / 25)) * 25)
        )

    car_manager.move_cars()

    for car in car_manager.cars:
        if (player.distance(car) <= 35) and ((car.ycor() - 15) <= player.ycor() <= (car.ycor() + 10)):
            running = False
            break

    if player.ycor() >= WINNING_Y_COR:
        next_level()

    screen.update()

screen.exitonclick()
