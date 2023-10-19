from turtle import Turtle
from env import WIDTH, HEIGHT

class Paddle(Turtle):
    
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(pos)

    def go_up(self):
        if self.ycor() + 20 <= abs(self.ycor()):
            self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        if self.ycor() + 20 <= abs(self.ycor()):
            self.goto(self.xcor(), self.ycor() - 20)
    
    def resize(self, width, height, new_width, new_height):
        diff_w = new_width - width
        diff_h = new_height - height
        x = self.xcor() + diff_w / 2
        y = self.ycor() + diff_h / 2
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto((x, y))