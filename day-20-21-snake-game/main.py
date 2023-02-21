# from turtle import Turtle, Screen
# import time
#
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My snake game")
# screen.tracer(0)
# colors = ['blue', 'red', 'white']
# positions = [0, -20, -40]
# final_snake = []
#
# for index in range(3):
#     snake = Turtle(shape='square')
#     snake.color(colors[index])
#     snake.penup()
#     snake.goto(x=positions[index], y=0)
#     final_snake.append(snake)
#
# while True:
#     screen.update()
#     time.sleep(1)
#     for segment in range(len(final_snake) - 1, 0, -1):
#         new_x = final_snake[segment - 1].xcor()
#         new_y = final_snake[segment - 1].ycor()
#         final_snake[segment].goto(new_x, new_y)
#     final_snake[0].forward(10)
#     final_snake[0].right(90)
#
#
#
# screen.exitonclick()

from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from text import Text

score = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
turtle = Turtle()


snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
text = Text()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.random_location()
        snake.extend()
        text.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -300:
        text.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            text.game_over()
















screen.exitonclick()