from turtle import *
import random

line = Turtle()
screen = Screen()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_col = (r,g,b)
    return random_col

def figure(num_sides, large):
    angle = 360 / num_sides
    for _ in range(num_sides):
        line.forward(large)
        line.right(angle)

for i in range(3,11):
    pencolor(random_color())
    line.color(random_color())
    figure(i,i*i)
screen.exitonclick()
