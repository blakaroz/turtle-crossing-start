import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
counter = 0

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate a new car in each 6 iteration
    if counter % 6 ==0:
        new_car = CarManager()

    # Move each car
    for car in CarManager.cars:
        car.car_move()
        car.car_remove()

    counter += 1


screen.exitonclick()