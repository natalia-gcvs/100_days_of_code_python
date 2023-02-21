import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()
        self.random_location()

    def create_food(self):
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')

    def random_location(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

