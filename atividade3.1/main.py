from turtle import *

t = Turtle()
t.speed(0)

# t.pu()
# t.goto(200,300)
# t.pd()
# for _ in range(4):
#     t.fd(100)
#     t.rt(90)

def des_quadr(x,y,lado,color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(4):
        t.fd(lado)
        t.rt(90)
    t.end_fill()

des_quadr(-200,200,200,"red")
des_quadr(50,0,100,"blue")

mainloop()