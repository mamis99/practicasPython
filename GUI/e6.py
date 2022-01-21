from turtle import *

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = 'Make your pet', prompt = 'Which turtle will win the race? ')

colors = ['red', 'orange', 'blue', 'yellow', 'green', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for index in range(6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[index])
    all_turtles.append(new_turtle)

screen.exitonclick()