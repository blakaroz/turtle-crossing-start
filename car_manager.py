from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

y_place = random.randint(-230,250)

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=20/20, stretch_len=40/20)
        self.goto(270,y_place)

    def car_move(self):
        new_x = self.xcor() + STARTING_MOVE_DISTANCE
        self.goto(y_place, new_x)