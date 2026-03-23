from turtle import *
import time

#t.fillcolor()
#t.beginfill()
t= Turtle()
t.speed(0)

#bandeira1

t.pu()
t.goto(-300,-100)
t.pd()

for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.pu()
t.goto(0,-30)
t.pd()
t.fillcolor("red")
t.begin_fill()
t.circle(80)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira2

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira3

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("green")
t.begin_fill()
t.lt(90)
for _ in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira4

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("orange")
t.begin_fill()
t.lt(90)
for _ in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira5

t.pu()
t.goto(-300,-100)
t.pd()
t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.rt(90)
t.end_fill()

t.pu()
t.goto(-20,20)
t.pd()
t.fillcolor("white")
t.begin_fill()
for _ in range(4):
    t.fd(60)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.fd(60)
    t.rt(90)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira 6

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("black")
t.begin_fill()
t.lt(90)
for _ in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.end_fill()
t.lt(90)
time.sleep(3)
t.clear()

#bandeira7

t.pu()
t.goto(-300,-100)
t.pd()

for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.fillcolor("red")
t.begin_fill()
t.lt(90)
t.fd(150)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(600)
t.end_fill()
t.rt(90)
t.rt(90)
time.sleep(3)
t.clear()

#bandeira8

t.pu()
t.goto(-300,-100)
t.pd()

for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.fillcolor("blue")
t.begin_fill()
t.lt(90)
t.fd(200)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(600)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(600)
t.end_fill()
t.rt(180)
time.sleep(3)
t.clear()

#bandeira9

t.pu()
t.goto(-300,-100)
t.pd()
t.fillcolor("black")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("red")
t.begin_fill()
t.lt(90)
t.fd(200)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(600)
t.end_fill()

t.fillcolor("yellow")
t.begin_fill()
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(600)
t.end_fill()
t.rt(180)
time.sleep(3)
t.clear()

t.pu()
t.goto(-300,-100)
t.pd()
t.fillcolor("#0057B7")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()
t.fillcolor("yellow")
t.begin_fill()
t.lt(90)
t.fd(150)
t.rt(90)
t.fd(600)
t.rt(90)
t.fd(150)
t.rt(90)
t.fd(600)
t.end_fill()
t.rt(180)
time.sleep(3)
t.clear()

#bandeira11

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("green")
t.begin_fill()
for _ in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.lt(90)
t.end_fill()

t.fillcolor("green")
t.begin_fill()
t.fd(400)
t.lt(90)
t.fd(300)
t.lt(90)
t.fd(200)
t.lt(90)
t.fd(300)
t.end_fill()
t.rt(270)
time.sleep(3)
t.clear()

#bandeira12

t.pu()
t.goto(-300,-100)
t.pd()

t.fillcolor("red")
t.begin_fill()
for _ in range(2):
     t.fd(600)
     t.lt(90)
     t.fd(300)
     t.lt(90)
t.end_fill()

t.pu()
t.goto(-100, -50)
t.color("white")
t.pd()
t.begin_fill()
t.circle(80)
t.end_fill()

t.pu()
t.goto(-70, -50)
t.color("red")
t.pd()
t.begin_fill()
t.circle(60)
t.end_fill()

t.pu()
t.goto(40, 10)
t.color("white")
t.pd()

t.begin_fill()
for _ in range(5):
    t.fd(80)
    t.lt(144)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira13

t.pu()
t.goto(-300,-150)
t.pd()

t.fillcolor("green")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(0, 120)
t.pd()

t.fillcolor("yellow")
t.begin_fill()

t.goto(150, 0)
t.goto(0, -120)
t.goto(-150, 0)
t.goto(0, 120)

t.end_fill()

t.pu()
t.goto(0, -80)
t.pd()

t.fillcolor("blue")
t.begin_fill()
t.circle(80)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira14

t.pu()
t.goto(-300, -100)
t.setheading(0)
t.pd()

t.fillcolor("skyblue")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(100)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 0)
t.pd()

t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(100)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 100)
t.pd()

t.fillcolor("skyblue")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(100)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(0, 20)
t.pd()

t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira15

t.pu()
t.goto(-300, -100)
t.setheading(0)
t.pd()

t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-100, -100)
t.pd()

t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.fd(60)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 0)
t.pd()

t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(60)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-80, -100)
t.pd()

t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.fd(30)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 15)
t.pd()

t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(30)
    t.lt(90)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira16

t.pu()
t.goto(-300, -100)
t.setheading(0)
t.pd()

t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-100, -100)
t.pd()

t.fillcolor("yellow")
t.begin_fill()
for _ in range(2):
    t.fd(60)
    t.lt(90)
    t.fd(300)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 0)
t.pd()

t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(60)
    t.lt(90)
t.end_fill()
time.sleep(3)
t.clear()

#bandeira17

t.pu()
t.goto(-300, -100)
t.setheading(0)
t.pd()

t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 50)
t.pd()

t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.fd(600)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-300, 50)
t.pd()

t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.fd(150)
    t.lt(90)
    t.fd(150)
    t.lt(90)
t.end_fill()

t.pu()
t.goto(-225, 100)
t.pd()

t.fillcolor("white")
t.begin_fill()
for _ in range(5):
    t.fd(60)
    t.lt(144)
t.end_fill()
time.sleep(3)
t.clear()

mainloop()