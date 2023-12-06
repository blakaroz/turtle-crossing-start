import time, player
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
#finish_line_y = 0

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
counter = 0

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

# Detect if collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

# Detect if level completed
    if player.ycor() >= player.finish_line:
         player.new_level()
         scoreboard.level_up()
         car_manager.car_speed_up()

screen.exitonclick()
