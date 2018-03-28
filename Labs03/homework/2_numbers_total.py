from random import randint
from turtle import *
shape('turtle')
speed(-1)
color('purple')

def totals(x, y):
    write('{0}+{1}={2}'.format(x, y, x+y), font=("Arial", 20, "normal"))
    ht()
    
x = randint(0, 100)
y = randint(0, 100)
totals(x, y)
mainloop()
