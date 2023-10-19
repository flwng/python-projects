from env import WIDTH, HEIGHT
from turtle import Turtle

DISTANCE = 10

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        self.fd(DISTANCE)
    
    # def paddle_collision(paddle_x_cor, paddle_y_cor):
