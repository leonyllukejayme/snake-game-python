from turtle import Turtle
FONT = ('Arial',24, 'normal')
ALIGN = 'center'

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,260)
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.write(f"Score: {self.score}", align=ALIGN,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGN,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreBoard()
