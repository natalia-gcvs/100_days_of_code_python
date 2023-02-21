from turtle import Turtle


class State(Turtle):
    def __init__(self, x_pos, y_pos, state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)
        self.write(state)
