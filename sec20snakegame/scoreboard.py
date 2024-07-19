#importing modules
from turtle import Turtle

#creating a scoreboard class
class Scoreboard(Turtle):

    #constructor of scoreboard class
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.color('white')

    def turtle_write(self):
        self.current_score+=1
        self.clear()
        self.write(f'score = {self.current_score}', False, align='center',font=('Arial', 12, 'normal'))
