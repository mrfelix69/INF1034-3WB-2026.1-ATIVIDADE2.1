from turtle import *

t = Turtle()
t.speed(0)
from time import sleep

# def desenha_triang(x,y,larg,alt,color):
#     t.pu()
#     t.goto(x,y)
#     t.pd()

#     t.begin_fill()
#     t.fillcolor(color)
#     for _ in range(2):
#         t.fd(larg)
#         t.rt(90)
#         t.fd(alt)
#         t.rt(90)
#     t.end_fill()

# def desenha_bandeira_fra():
#     desenha_triang(-200,200,50,150,"red")
#     desenha_triang(-150,200,50,150,"white")
#     desenha_triang(-100,200,50,150,"blue")

# desenha_bandeira_fra()
# sleep(3)
# t.clear()

#bandeira1(japao)

def desenha_ret(x,y,larg,alt,color):
    t.pu()
    t.goto(x,y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.fd(larg)
        t.lt(90)
        t.fd(alt)
        t.lt(90)
    t.end_fill()

def desenh_circ(x1,y1,tamanho,colorjp):
    t.pu()
    t.goto(x1,y1)
    t.pd()

    t.begin_fill()
    t.fillcolor(colorjp)
    t.circle(tamanho)
    t.end_fill()

def desenha_bandeira_jap():
    desenha_ret(-300,-100,600,300,"white")

desenha_bandeira_jap()
desenh_circ(0,-25,80,"red")
# sleep(3)
t.clear()

#bandeira2 (frança)

def desenha_bandeira_fra():
    desenha_ret(-300,-100,600,300,"#000091")
    desenha_ret(-100,-100,400,300,"white")
    desenha_ret(100,-100,200,300,"#E1000F")

desenha_bandeira_fra()
#
t.clear()


#bandeira3(italia)

def desenha_bandeira_ita():
    desenha_ret(-300,-100,600,300,"#008C45")
    desenha_ret(-100,-100,400,300,"white")
    desenha_ret(100,-100,200,300,"#CD212A")

desenha_bandeira_ita()

t.clear()

#bandeira4(costamarfim)

def desenha_bandeira_costmarf():
    desenha_ret(-300,-100,600,300,"#FF8200")
    desenha_ret(-100,-100,400,300,"white")
    desenha_ret(100,-100,200,300,"#009E60")

desenha_bandeira_costmarf()

t.clear()

#bandeira5(suica)

def desenha_bandeira_suica():
    desenha_ret(-300,-100,600,300,"red")

def des_cruz(x5,y5,lado,colorcruz):
    t.pu()
    t.goto(x5,y5)
    t.pd()
    t.fillcolor(colorcruz)
    t.begin_fill()
    for _ in range(4):
        t.fd(lado)
        t.lt(90)
        t.fd(lado)
        t.lt(90)
        t.fd(lado)
        t.rt(90)
    t.end_fill()

desenha_bandeira_suica()
des_cruz(30,20,60,"white")

t.clear()

#bandeira6(belgica)

def des_bandeira_bel():
    desenha_ret(-300,-100,600,300,"black")
    desenha_ret(-100,-100,400,300,"#FFCD00")
    desenha_ret(100,-100,200,300,"#C8102E")

des_bandeira_bel()

t.clear()

#bandeira7(polonia)

def des_bandeira_pol():
    desenha_ret(-300,-100,600,300,"white")
    desenha_ret(-300,-100,600,150,"#DC143C")

des_bandeira_pol()
#
t.clear()

#bandeira8(russia)

def des_bandeira_rus():
    desenha_ret(-300,-100,600,300,"white")
    desenha_ret(-300,-100,600,200,"#0036A7")
    desenha_ret(-300,-100,600,100,"#D62718")

des_bandeira_rus()

#bandeira9(alemanha)

def des_bandeira_alema():
    desenha_ret(-300,-100,600,300,"#000000")
    desenha_ret(-300,-100,600,200,"#DD0000")
    desenha_ret(-300,-100,600,100,"#FFCE00")

des_bandeira_alema()
#
t.clear()

#bandeira10(nigeria)

def des_bandeira_nig():
    desenha_ret(-300,-100,600,300,"#008751")
    desenha_ret(-100,-100,400,300,"white")
    desenha_ret(100,-100,200,300,"#008751")

des_bandeira_nig()

t.clear()

#bandeira11(turquia)

def des_bandeira_turq():
    desenha_ret(-300,-100,600,300,"red")

def lua_turq(x11,y11,tamanho11,color11):
    t.pu()
    t.goto(x11,y11)
    t.fillcolor(color11)
    t.pd()
    t.begin_fill()
    t.circle(tamanho11)
    t.end_fill()

def lua_turq2(xt11,yt11,tamanhot11,colort11):
    t.pu()
    t.goto(xt11,yt11)
    t.fillcolor(colort11)
    t.pd()
    t.begin_fill()
    t.circle(tamanhot11)
    t.end_fill()

def estrela_turq(xe11,ye11,tamanhoe11,colore11):
    t.pu()
    t.goto(xe11, ye11)
    t.color(colore11)
    t.pd()

    t.begin_fill()
    for _ in range(5):
        t.fd(tamanhoe11)
        t.lt(144)
    t.end_fill()

des_bandeira_turq()
lua_turq(-100,-50,80,"white")
lua_turq2(-70,-50,60,"red")
estrela_turq(40,10,80,"white")

t.clear()

#bandeira12(brasil)

def des_bandeira_bra():
    desenha_ret(-300,-150,600,300,"#009440")

def des_losang_br():
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

def des_bola_br(xb12,yb12,tamanhobr12,colorbr):
    t.pu()
    t.goto(xb12,yb12)
    t.pd()

    t.fillcolor(colorbr)
    t.begin_fill()
    t.circle(tamanhobr12)
    t.end_fill()

des_bandeira_bra()
des_losang_br()
des_bola_br(0,-80,80,"#302681")


mainloop()
