from turtle import Turtle
import random

COLORS = ['yellow', 'blue', 'red', 'orange', 'purple', 'green']
STARTING_MOVE_SPEED = 5
MOVE_SPEED_INCREMENT = 10


class Cars:

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape='square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            car.goto(300, y_pos)
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_SPEED)

    def increase_speed(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_SPEED_INCREMENT
            car.goto(new_x, car.ycor())



