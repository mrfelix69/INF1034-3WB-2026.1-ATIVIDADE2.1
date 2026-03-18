from turtle import *


t = Turtle()

#isso é um quadrado
#for _ in range(4):
    #t.fd(100)
    #t.lt(90)

#plano cartesiano

t.pu()
t.goto(0,0)
t.pd()
t.fd(300)
t.stamp()
t.lt(180)
t.fd(600)
t.stamp()
t.lt(180)
t.fd(300)
t.lt(90)
t.fd(300)
t.stamp()
t.lt(180)
t.fd(600)
t.stamp()

#quadrante 1 

t.pu()
t.goto(170,200)
t.pd()
t.fd(100)
t.lt(115)
t.fd(70)
t.lt(90)
t.fd(70)

mainloop()
