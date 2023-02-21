from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# SEGMENT_COLORS = ['red', 'blue', 'yellow']
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.append_segment(position)

    def append_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        # print(len(self.segments))

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.append_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(RIGHT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(LEFT)



