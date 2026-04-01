from turtle import *
from time import *

# def soma_2(x):
#     return x + 2
#elevX = 2^x

def raizX(x):
    return x**0.5

def sobX(x):
    return 1/x

def func3(x):
    return 2**x

def func4(x):
    return 5-func3

def func5(x):
    return func3-5*x+6

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

#função 

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
    t.goto(x*2,raizX(x*2))

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
    t.goto(x,sobX(x/50)*8)

for x in range(1,299):
    t.goto(x,sobX(x/50)*8)

sleep(2)
t.clear()

#função 3 

t.rt(90)
t.color('black')
des_plancart()

t.pu()
t.goto(-299,0)
t.pd()

for x in range(-299,200):
    t.goto(x,func3(x))
    
sleep(2)
t.clear()

t.rt(90)
des_plancart()

















mainloop()