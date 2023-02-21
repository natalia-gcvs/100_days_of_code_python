from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-200, 270)
        self.write(f"Level: {self.level}", True, font=('Courier', 15, 'bold'))

    def display_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 270)
        self.write(f"Level: {self.level}", True, font=('Courier', 15, 'bold'))

    def game_over(self):
        self.goto(-80, 0)
        self.write('Game Over', True, font=('Courier', 20, 'bold'))



