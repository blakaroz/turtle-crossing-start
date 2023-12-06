from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
y_place = random.randint(-230,250)

class CarManager(Turtle):
    cars = []
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=20/20, stretch_len=40/20)
        y_place = random.randint(-230, 250)
        self.goto(270,y_place)
        self.setheading(180)
        CarManager.cars.append(self)

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)


    def car_remove(self):
        # Check if the car is beyond the left edge of the screen
        if self.xcor() < -300:
            CarManager.cars.remove(self)
            self.hideturtle()

