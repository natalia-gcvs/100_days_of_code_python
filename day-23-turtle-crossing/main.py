from turtle import Turtle, Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, 'Up')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if player.ycor() > 270:
        car.increase_speed()
        scoreboard.display_level()
        player.reset_position()
    for i in car.cars:
        if player.distance(i) < 25:
            game_is_on = False
            scoreboard.game_over()














screen.exitonclick()

