#importing turtle modules
from turtle import Turtle, Screen
import random

#functions
# def move_forward():
#     chinni.forward(100)

# def move_backward():
#     chinni.backward(100)

# def turn_counter_clockwise():
#     chinni.left(90)

# def turn_clockwise():
#     chinni.right(90)

# def clear_drawing():
#     chinni.clear()
#     chinni.reset()

#implementation
#creating turtle, screen objects
chinni = Turtle()

is_race_on = False
my_screen = Screen()
my_screen.setup(height=500, width=500)
user_bet = my_screen.textinput(title='make ur bet', prompt='which turtle will win the race? enter the color: ')

#implementing screen listen and binding key - etch a sketch
my_screen.listen()
# my_screen.onkey(key='W', fun=move_forward)
# my_screen.onkey(key='S', fun=move_backward)
# my_screen.onkey(key='A', fun=turn_counter_clockwise)
# my_screen.onkey(key='D', fun=turn_clockwise)
# my_screen.onkey(key='C', fun=clear_drawing)

#turtlerace
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10,  20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'you have won: winner is {winning_color} turtle')
            else:
                print(f'you have lost: winner is {winning_color} turtle')

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


#turtle coordinate System
#exit on click function
my_screen.exitonclick()