import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
turtle.colormode(255)

colours = ['firebrick', 'plum', 'blue', 'red', 'orange', 'purple', 'yellow', 'green']

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
#
#
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed('fastest')

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(i)


# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
