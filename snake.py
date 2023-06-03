import time
from turtle import Turtle, Screen
LOCATION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIC = 20
WIDTH = 600
HIEGTH = 600
class Snake():

    def __init__(self):
        self.segments = []
        self.set_head()
        self.head = self.segments[0]

    def set_screen(self):
        self.screen.tracer(0)
        self.screen.setup(WIDTH, HIEGTH)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")



    def set_head(self):
        for place in LOCATION:
            self.add_seg(place)


    def add_seg(self,location):
        new_pace = Turtle("square")
        new_pace.penup()
        new_pace.goto(location)
        new_pace.color("white")
        self.segments.append(new_pace)


    def extend(self):

        self.add_seg(self.segments[-1].position())



    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DIC)

    def out_of_screen(self):
        if self.head.xcor() <= -WIDTH or self.head.xcor() >= WIDTH/2or self.head.ycor() <= -HIEGTH/2 or self.head.ycor() >= HIEGTH/2:
            return True
        return False

    def colotion(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < 5 :
                return True

    def reset(self):
        for seg in self.segments:
            seg.goto(500,500)
        self.segments.clear()
        self.set_head()
        self.head = self.segments[0]
