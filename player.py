from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line_y = -40

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)
    
    def new_level(self):
        self.goto(STARTING_POSITION)

    
