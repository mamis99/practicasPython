from turtle import *
import random

line = Turtle()
screen = Screen()

screen.setup(500, 400)
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r,g,b)
    return random_col

def forward():
    line.forward(20)
    line.color(random_color())

def backward():
    line.backward(20)
    line.color(random_color())

def right():
    new_heading = line.heading() + 10
    line.setheading(new_heading)
    line.color(random_color())

def left():
    new_heading = line.heading() - 10
    line.setheading(new_heading)
    line.color(random_color())

screen.listen()
screen.onkey(forward,'w')
screen.onkey(backward,'s')
screen.onkey(left,'d')
screen.onkey(right,'a')
screen.mainloop()