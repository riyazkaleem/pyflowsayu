#importing modules
from turtle import Turtle

#creating a scoreboard class
class Scoreboard(Turtle):

    #constructor of scoreboard class
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')

    #this method is to display the title and the score card
    def turtle_write(self):
        self.goto(0,280)
        self.current_score+=1
        self.clear()
        self.write(f'score = {self.current_score}', False, align='center',font=('Arial', 12, 'normal'))

    #this method is to display the game over message
    def gameover(self):
        self.goto(0,0)
        self.write(f'Game over', False, align='center',font=('Arial', 12, 'normal'))
