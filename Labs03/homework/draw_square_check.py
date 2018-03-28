from draw_square import draw_square
from turtle import *
shape('turtle')
speed(-1)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
