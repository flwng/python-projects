from turtle import Turtle

DISTANCE = 20
INITIAL_POS = [(0, 0), (-20, 0), (-40, 0)]

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
    
    def create_snake(self):
        for position in INITIAL_POS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].fd(DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def eaten_food(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()                   
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
    
    def self_eat(self):
        for segment in self.segments[1:]:
            if self.segments[0].distance(segment) < 1:
                return True
        return False

    def reset(self):
        self.segments.clear()
        self.create_snake()