from turtle import Screen, Turtle
from snake import Snake
from score import Score
from food import Food
import time

# TOP_BORDER = 260

def init():

    screen.clear()
    screen.bgcolor('black')
    screen.tracer(0)

    top_border = Turtle()
    top_border.color('white')
    top_border.penup()
    top_border.goto(-300, 260)
    top_border.pendown()
    top_border.goto(300, 260)
    top_border.penup()

    snake = Snake()
    food = Food()
    score = Score()

    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.right, 'Right')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(init, 'space')

    game_on = True

    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect self collision
        if snake.self_eat():
            game_on = False
            score.game_over()

        # detect border collision
        if snake.segments[0].xcor() >= 300 or snake.segments[0].xcor() <= -320 or snake.segments[0].ycor() <= -300 or snake.segments[0].ycor() >= 260:
            game_on = False
            score.game_over()

        # detect food collision
        if snake.segments[0].distance(food) < 1:
            snake.eaten_food()
            score.update_score()
            food.refresh()



if __name__ == '__main__':
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.tracer(0)

    start = Turtle()
    start.color('white')
    start.penup()
    start.goto(0, 0)
    start.write(f"Press Spacebar to start", align='center', font=('Arial', 40, 'normal'))

    screen.listen()
    screen.onkeypress(init, 'space')

    screen.exitonclick()
    screen.mainloop()