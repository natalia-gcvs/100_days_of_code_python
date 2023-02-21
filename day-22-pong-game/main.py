from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

# def move_forward():
#     segment.right(90)
#     segment.forward(10)
# segment = Turtle('square')
# segment.penup()
# segment.color('white')
# segment.goto(350, 0)
#
# screen.onkey(fun=move_forward, key='Up')
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-100, 250))
r_scoreboard = Scoreboard((100, 250))

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.back_to_center()
        l_scoreboard.increase_score()

    if ball.xcor() < -380:
        ball.back_to_center()
        r_scoreboard.increase_score()

















screen.exitonclick()