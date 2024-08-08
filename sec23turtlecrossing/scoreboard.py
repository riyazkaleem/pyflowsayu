#importing modules
from turtle import Turtle
FONT = ("Courier", 24, "normal")

#declaring the scoreboard class
class Scoreboard(Turtle):
    
    #declaring the constructor
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 260)
        self.write(f'Level: {self.level}', align = 'left', font=FONT)

    #update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f'level: {self.level}', align='left', font=FONT)

    #increase level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    #game over
    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over', align='center', font=FONT)
    