from turtle import *
def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        forward(100)
        right(144)
    ht()
