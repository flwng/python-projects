from turtle import Screen
from snake import Snake
from food import Food
import time

# class Snake:

#     def __init__(self):
#         self.segments = []
#         self.create_snake()
    
#     def create_snake(self):
#         for position in INITIAL_POS:
#             new_segment = Turtle('square')
#             new_segment.color('white')
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
    
#     def move(self):
#         for i in range(len(self.segments) - 1, 0, -1):
#             x = self.segments[i - 1].xcor()
#             y = self.segments[i - 1].ycor()
#             self.segments[i].goto(x, y)
#         self.segments[0].fd(DISTANCE)

#     def up(self):
#         if self.segments[0].heading != 270:
#             self.segments[0].setheading(90)

#     def down(self):
#         if self.segments[0].heading != 90:
#             self.segments[0].setheading(270)

#     def left(self):
#         if self.segments[0].heading != 0:
#             self.segments[0].setheading(180)

#     def right(self):
#         if self.segments[0].heading != 180:
#             self.segments[0].setheading(0)




screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.left, 'Left')

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()