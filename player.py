from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE 

    def go_up(self):
        self.forward(MOVE_DISTANCE)
    
    def new_level(self):
        self.goto(STARTING_POSITION)

    
