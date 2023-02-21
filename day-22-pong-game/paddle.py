from turtle import Turtle

SEGMENT_POSITIONS = [-40, -20, 0, 20, 40]
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color('white')
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        print(f"xcor: {self.xcor()}")
        print(f"ycor: {self.ycor()}")
        self.goto(self.xcor(), new_y)
        print(f"2xcor: {self.xcor()}")
        print(f"2ycor: {self.ycor()}")


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



