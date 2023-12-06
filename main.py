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
    # Detect collision with car
        #if player.distance(car) < 10:
        if (
            player.xcor() - 20 < car.xcor() < player.xcor() + 20
            and player.ycor() - 20 < car.ycor() < player.ycor() + 20
            ):
            game_is_on = False
            scoreboard.game_over()
    #CarManager.check_colision()
    counter += 1



    if player.ycor() >= player.finish_line_y:
        player.new_level()
        scoreboard.level_up()
        # still wrong  i want that every car which is on screen to speed up

        # for car in CarManager.cars:
        #     car.car_speed_up()

screen.exitonclick()