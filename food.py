from turtle import Turtle
import random
WIDTH = 600
HIEGHT = 600
class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.x_cor = random.randint(-280,280)
        self.y_cor = random.randint(-280,280)
        self.goto(self.x_cor,self.y_cor)



