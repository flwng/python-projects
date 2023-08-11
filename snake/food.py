from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('pink')
        self.speed('fastest')
        x = random.randrange(-280, 240, 20)
        y = random.randrange(-280, 240, 20)
        self.goto(x, y)

    def refresh(self):
        x = random.randrange(-280, 240, 20)
        y = random.randrange(-280, 240, 20)
        self.goto(x, y)