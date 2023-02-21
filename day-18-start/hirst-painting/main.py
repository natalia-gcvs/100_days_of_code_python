import turtle

import colorgram as cg
from turtle import Turtle, Screen
import random

colors = cg.extract("hirst.jpg", 2 ** 32)
color_palette = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_palette.append(rgb)

print(color_palette)
print(colors)

rgb_colors = [(244, 159, 35), (14, 95, 184), (209, 75, 99), (46, 128, 56), (158, 6, 57), (253, 223, 0), (232, 169, 8), (224, 116, 165), (244, 218, 48), (14, 59, 143), (96, 203, 187), (10, 15, 81), (242, 155, 174), (75, 37, 8), (2, 115, 46), (164, 172, 189), (15, 180, 9), (89, 74, 197), (119, 1, 91), (182, 55, 83), (214, 91, 21), (246, 174, 172), (225, 82, 43), (185, 188, 204), (138, 217, 188), (56, 149, 189), (94, 60, 28), (145, 207, 231), (98, 52, 42), (0, 82, 17), (8, 77, 116)]

pen = Turtle()
turtle.colormode(255)

pen = turtle.Turtle()
pen.setheading(180)

# pen.dot(10, random.choice(rgb_colors))
# pen.forward(20)
# pen.dot(10, random.choice(rgb_colors))
# pen.forward(20)


# method to draw rectangle with dots
# space --> distance between dots
# x     --> height of rectangle
# y     --> width of rectangle
def draw(space, x, y):
    for i in range(x):
        for j in range(y):
            # dot
            pen.setheading(270)
            pen.dot(20, random.choice(rgb_colors))

            # distance for another dot
            
            pen.forward(space)
        pen.backward(space * y)

        # direction
        pen.right(90)
        pen.forward(space)
        pen.left(90)


# Main Section
pen.penup()
draw(30, 10, 10)

# hide the turtle
pen.hideturtle()


screen = Screen()
screen.exitonclick()