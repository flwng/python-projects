from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from env import WIDTH, HEIGHT
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

paddle1 = Paddle((-(WIDTH / 2) + 50,0))
paddle2 = Paddle((WIDTH / 2 - 50,0))

ball = Ball()

screen.listen()
screen.onkey(paddle2.go_up, 'Up')
screen.onkey(paddle2.go_down, 'Down')
screen.onkey(paddle1.go_up, 'w')
screen.onkey(paddle1.go_down, 's')

while True:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # collision detection
    if abs(ball.xcor()) >= WIDTH / 2:
        game_over = Turtle()
        game_over.color('red')
        game_over.goto(0, 0)
        if ball.xcor() > 0:
            game_over.write('Player 2 Wins', align='center', font=('Arial', 32, 'normal'))
        else:
            game_over.write('Player 1 Wins', align='center', font=('Arial', 32, 'normal'))

    # collision with paddle
    

screen.exitonclick()