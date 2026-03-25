from turtle import *
from random import *


t = Turtle()
t.speed(0)


#plano cartesiano
def plan_cart(x,y,frente,tras):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fd(frente) #300
    t.stamp()
    t.bk(tras) #600
    t.lt(180)
    t.stamp()
    t.lt(180)
    t.fd(frente) #300
    t.lt(90) 
    t.fd(frente) #300
    t.stamp()
    t.bk(tras) #600
    t.lt(180)
    t.stamp()
    t.lt(90)

plan_cart(0,0,300,600)


#quadrante 1 (triangulo)
x1 = randint(100,200)
y1 = randint(100,200)
color1 = textinput('Obter cor:', 'Digite a cor do triângulo:')
def quadr1_triang(x1,y1,lado,color1):
    t.pu()
    t.goto(x1,y1)
    t.pd()
    t.color("black")
    t.fillcolor(color1)
    t.begin_fill()

    for _ in range(3):
        t.fd(lado)
        t.lt(120)

    t.end_fill()
quadr1_triang(x1,y1,200,color1)

#quadrante 2 (retangulo)
x2 = randint(-170,-125)
y2 = randint(100,200)
color2 = textinput('Obter cor:', 'Digite a cor do retângulo')
def quadr2_retang(x2,y2,ladomaior,ladomenor,color2):
    t.pu()
    t.goto(x2,y2)
    t.pd()

    t.color('black')
    t.fillcolor(color2)
    t.begin_fill()

    for _ in range(2):
        t.fd(ladomaior)
        t.lt(90)
        t.fd(ladomenor)
        t.lt(90)

    t.end_fill()
quadr2_retang(x2,y2,100,50,color2)

#quadrante 3 (pentagono)
x3 = randint(-170,-100)
y3 = randint(-200,-150)
color3 = textinput('Digite a cor', 'Digite a cor do pentagono')
def quadr3_pent(x3,y3,lado,color3):
    t.color('black')
    t.fillcolor(color3)
    t.begin_fill()

    t.pu()
    t.goto(x3,y3)
    t.pd()

    for _ in range(5):
        t.fd(lado)
        t.lt(72)

    t.end_fill()
quadr3_pent(x3,y3,70,color3)

#quadrante 4 (hexagono)
x4 = randint(100,250)
y4 = randint(-200,-150)
color4 = textinput('Digite a cor', 'Digite a cor do hexágono')
def quadr4_hexa(x4,y4,lado,color4):
    t.pu()
    t.goto(x4,y4) #120,-150
    t.pd()

    t.color('black')
    t.fillcolor(color4)
    t.begin_fill()

    for _ in range(6):
        t.fd(lado)
        t.lt(60)

    t.end_fill()
quadr4_hexa(x4,y4,70,color4)

#espiral (tentar)

t.pu()
t.goto(140,120)
t.pd()

for i in range(120):
    t.fd(1 + i * 0.2)
    t.lt(10)

color5 = textinput('Obter cor:', 'Digite a cor do poligono:')
def desenhar_polig(x,y,numerolado,tamanholado,color5):
    t.pu()
    t.goto(x,y)
    t.pd()
    ang = 360/numerolado

    t.color('black')
    t.fillcolor(color5)
    t.begin_fill()

    for _ in range(numerolado):
        t.fd(tamanholado)
        t.lt(ang)
    t.end_fill()

desenhar_polig(0,0,10,70,color5)


mainloop()