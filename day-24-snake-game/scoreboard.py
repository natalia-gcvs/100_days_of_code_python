from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(-20, 270)
        self.color('white')
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()



