from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 30, 'bold')


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(position)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

