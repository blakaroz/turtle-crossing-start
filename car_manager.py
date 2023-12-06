from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=20/20, stretch_len=40/20)
            y_place = random.randint(-230, 250)
            new_car.goto(270,y_place)
            self.all_cars.append(new_car)
            new_car.setheading(180)
    

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)


    def car_remove(self):
        # Check if the car is beyond the left edge of the screen
        if self.xcor() < -300:
            CarManager.cars.remove(self)
            self.hideturtle()
    
    def car_speed_up(self):
        self.car_speed += MOVE_INCREMENT
    

    
