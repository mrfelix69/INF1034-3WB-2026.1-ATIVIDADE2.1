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
t.lt(90)

#quadrante 1 (triangulo)

color1 = textinput('Digite a cor', 'Digite a cor do triângulo')
t.pu()
t.goto(100,100)
t.pd()

t.color("black")
t.fillcolor(color1)
t.begin_fill()

for _ in range(3):
    t.fd(100)
    t.lt(120)

t.end_fill()

#quadrante 2 (retangulo)
color2 = textinput('Digite a cor', 'Digite a cor do retângulo')

t.pu()
t.goto(-170,100)
t.pd()

t.color('black')
t.fillcolor(color2)
t.begin_fill()

for _ in range(2):
    t.fd(120)
    t.lt(90)
    t.fd(60)
    t.lt(90)

t.end_fill()

#quadrante 3 (pentagono)
color3 = textinput('Digite a cor', 'Digite a cor do pentagono')

t.pu()
t.goto(-170,-150)
t.pd()

t.color('black')
t.fillcolor(color3)
t.begin_fill()

t.pu()
t.goto(-150, -150)
t.pd()

for _ in range(5):
    t.fd(80)
    t.lt(72)

t.end_fill()

#quadrante 4 (hexagono)
color4 = textinput('Digite a cor', 'Digite a cor do hexágono')

t.pu()
t.goto(120,-150)
t.pd()

t.color('black')
t.fillcolor(color4)
t.begin_fill()

for _ in range(6):
    t.fd(80)
    t.lt(60)

t.end_fill()

t.speed(0)

#espiral (tentar)

t.pu()
t.goto(140,120)
t.pd()

for i in range(120):
    t.fd(1 + i * 0.2)
    t.lt(10)

mainloop()
