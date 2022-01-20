from turtle import *
import random

line = Turtle()
screen = Screen()
colormode(255)   #Se usa para poder utilizar hex

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw(size):
    angle = random.randint(0, 3) * 90
    line.forward(size)
    line.setheading(angle)
    line.color(random_color())

line.speed("fastest")
line.pensize(10)
for i in range(300):
    draw(30)