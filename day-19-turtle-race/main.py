from turtle import Turtle, Screen
import turtle

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)

def clockwise():
    tim.right(10)

def back_to_center():
    turtle.mode('standard')





screen.listen()


def control_turtle(key, func):
    screen.onkey(key=key, fun=func)


control_turtle('w', move_forwards)
control_turtle('s', move_backwards)
control_turtle('a', counter_clockwise)
control_turtle('d', clockwise)
control_turtle('c', back_to_center)


screen.exitonclick()


