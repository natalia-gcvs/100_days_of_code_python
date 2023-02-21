from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        y_new = self.ycor() + 10
        self.goto(0, y_new)

    def reset_position(self):
        self.goto(0, -280)



