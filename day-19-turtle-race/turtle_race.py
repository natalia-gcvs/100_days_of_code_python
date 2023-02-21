import random

from turtle import Turtle, Screen
import turtle


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True
while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color } turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
lista = [1, 1, 4, 5, 6]
random.shuffle(lista)

# tommy = Turtle(shape='turtle')
# tommy.color(colors[1])
# tommy.penup()
# tommy.goto(x=-240, y=-50)
#
# nina = Turtle(shape='turtle')
# nina.color(colors[2])
# nina.penup()
# nina.goto(x=-240, y=0)
#
# lulie = Turtle(shape='turtle')
# lulie.color(colors[3])
# lulie.penup()
# lulie.goto(x=-240, y=50)
#
# paty = Turtle(shape='turtle')
# paty.color(colors[4])
# paty.penup()
# paty.goto(x=-240, y=100)
#
# larie = Turtle(shape='turtle')
# larie.color(colors[5])
# larie.penup()
# larie.goto(x=-240, y=150)


screen.listen()
screen.exitonclick()
