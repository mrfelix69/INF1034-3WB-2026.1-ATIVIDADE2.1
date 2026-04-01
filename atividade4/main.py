from turtle import *

def soma_2(x):
    return x + 2

t = Turtle()

t.pu()
t.goto(-300,0)
t.pd()
t.goto(300,0)
t.stamp()

t.pu()
t.goto(0,-300)
t.pd()
t.goto(0,300)
t.lt(90)
t.stamp()


mainloop()