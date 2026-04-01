from turtle import *
from time import *

#funçoes

def raizX(x):
    return x**0.5

def sobX(x):
    return 1/x

def func3(x):
    return 2**x

def func4(x):
    return 5-x**2

def func5(x):
    return x**2-5*x+6

def func6(x):
    return x**3-x**2-x+1

t = Turtle()
t.speed(0)

#plano cartesiano

def des_plancart():
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

des_plancart()

#função aula

# t.color('red')
# t.pu()
# t.goto(-200,soma_2(-200))
# t.pd()

# print(list(range(-100,100)))

# for x in range(-99,101):
#     t.goto(x*2,soma_2(x*2))

#função 1 

t.color('red')
t.pu()
t.goto(0,raizX(0))
t.pd()


for x in range(1,300):
    t.goto(x,raizX(x)*10)

sleep(2)
t.clear()

#função 2 

t.rt(90)
t.color('black')
des_plancart()

t.pu()
t.goto(-299,sobX(10))
t.pd()

for x in range(-299,0):
    t.goto(x,sobX(x/50)*10)

for x in range(1,299):
    t.goto(x,sobX(x/50)*10)

sleep(2)
t.clear()

#função 3 

t.rt(90)
t.color('black')
des_plancart()

t.pu()
t.goto(-100,0)
t.pd()

for x in range(-100,100):
    t.goto(x*2,func3(x/20)*10)
    
sleep(2)
t.clear()

#função 4

t.rt(90)
des_plancart()

t.pu()
t.goto(-100,func4(-10)*10)
t.pd()

for x in range(-100,100):
    t.goto(x*3, func4(x/10)*10)

sleep(2)
t.clear()

#função 5 

t.rt(90)
des_plancart()

t.pu()
t.goto(-100,func5(-10)*10)
t.pd()

for x in range(-100,100):
    t.goto(x*3, func5(x/10)*10)

sleep(2)
t.clear()

#função 6 

t.rt(90)
des_plancart()

t.pu()
t.goto(-100,func4(-10)*5)
t.pd()

for x in range(-200,200):
    t.goto(x*5, func6(x/10)*5)

sleep(2)
t.clear()

mainloop()
