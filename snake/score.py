from turtle import Turtle
import os

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.highest_score = HighestScore()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(-280, 270)
        self.write(f"SCORE: {str(self.score)}", align='left', font=('Arial', 20, 'normal'))
        self.hideturtle()
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE: {str(self.score)}", align='left', font=('Arial', 20, 'normal'))
        self.highest_score.update(self.score)
    
    def game_over(self):
        self.color('red')
        self.goto(0, 0)
        self.write('Game Over', align='center', font=('Arial', 32, 'normal'))
        if self.score == self.highest_score.score:
            self.highest_score.save_score()
    
    def reset(self):
        self.score = 0
        self.clear()
        self.write(f"SCORE: {str(self.score)}", align='left', font=('Arial', 20, 'normal'))
        self.highest_score.clear()
        self.highest_score.show_score()


class HighestScore(Turtle):
        
    def __init__(self):
        super().__init__()
        self.show_score()
    
    def show_score(self):
        if os.path.exists('score.txt'):
            with open('score.txt', 'r') as f:
                self.score = int(f.read())
                f.close()
        else:
            self.score = 0
        self.color('white')
        self.penup()
        self.goto(280, 270)
        self.write(f"HIGHEST SCORE: {str(self.score)}", align='right', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def update(self, score):
        if score > self.score:
            self.score = score
            self.clear()
            self.write(f"HIGHEST SCORE: {str(score)}", align='right', font=('Arial', 20, 'normal'))
    
    def save_score(self):
        with open('score.txt', 'w') as f:    
            f.write(str(self.score))
            f.close()