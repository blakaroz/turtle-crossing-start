from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200,260)
        self.level = 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game over!", False, "center", FONT)
    
    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)
        
