
from turtle import *
shape('turtle')
speed(-1)
color('purple')

def write_words(times, text):
    j = -50
    for i in range(times):
        write(text, font=("Arial", 20, "normal"))
        penup()
        goto(0,j)
        pendown()
        ht()
        j += -50

write_words(3, "Hello World")

mainloop()
