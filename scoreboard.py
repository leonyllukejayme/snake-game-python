from turtle import Turtle
import os.path
FONT = ('Arial',24, 'normal')
ALIGN = 'center'
PATH = './high_score.txt'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.print_high_score()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.update_scoreBoard()

    def print_high_score(self):
        print(os.path.isfile(PATH))
        if not os.path.isfile(PATH):
            self.high_score = 0
        else:
            str_high_score = open('high_score.txt')
            self.high_score = int(str_high_score.read())

    def update_high_score(self):
        if self.score > self.high_score:
            with open('high_score.txt','w') as file:
                file.write(f"{self.score}")
            str_high_score = open('high_score.txt')
            self.high_score = int(str_high_score.read())

    def update_scoreBoard(self):
        self.clear()
        self.goto(0,260)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN,font=FONT)

    def reset(self):
        self.score = 0
        self.update_scoreBoard()


    def game_over(self):
        self.update_high_score()
        self.update_scoreBoard()
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN,font=FONT)
        self.goto(0,-50)
        self.write(f"Press the 'Space' key to play again", align=ALIGN,font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.update_scoreBoard()
