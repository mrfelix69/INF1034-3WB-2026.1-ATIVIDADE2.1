from turtle import *
from random import randint


def randomColor():
    #escolhe 3 numero random pra cor 
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def drawSquare(size):
    # função criada separada para desenhar o quadrado

    pd()
    begin_fill() 
    fillcolor(randomColor())  #cor aleatória

    # repete 4 vezes para fazer os 4 lados
    for i in range(4):
        fd(size)
        rt(90)

    end_fill() 
    pu() 


# facil (espiral)

def drawEasy():
    pd()

    # i vai de 0 ate 49
    # cada volta aumenta o tamanho da linha
    for i in range(50):
        pencolor(randomColor())  # troca cor
        fd(i * 3)
        lt(91)  # gira para formar espiral

    pu()


# medio (arvore)

def drawTree(size, angle):
    # size = tamanho do galho
    # angle = angulo que vai abrir os ramos

    # quando ficar pequeno ele para
    if size < 15:
        return

    pd()
    fd(size)

    # ramo esquerdo
    lt(angle)
    drawTree(size - 12, angle)

    # ramo direito
    rt(angle * 2)
    drawTree(size - 12, angle)

    # volta para posição original
    lt(angle)
    back(size)
    pu()


# dificil (espiral com quadrados)

def drawSquareSpiral(size, step=60, angle=18):
    # size = tamanho do quadrado
    # step = quantas vezes repete
    # angle = angulo da espiral

    # condicao para parar
    if step <= 0 or size < 5:
        return

    drawSquare(size)

    # move um pouco para frente
    fd(size / 2)

    # gira para formar a espiral circular
    lt(angle)

    # chama a funcao novamente com quadrado menor
    drawSquareSpiral(size - 2, step - 1, angle)


# config

colormode(255)  # ativa a cor
speed(0)
pu()


# facil

goto(-300, 150)
setheading(0)  # direcao inicial
drawEasy()


# medio

goto(0, -200)
setheading(90)  # aponta para cima
pencolor("black")
drawTree(80, 25)


# dficil

goto(200, 0)
setheading(0)
drawSquareSpiral(100, 50, 18)

#extra

#apaga so o desenho da arvore e redesenha com novo angulo
def atualizarArvore(angle):
    clear()

    # redesenha os 3 fractais
    goto(-300, 150)
    setheading(0)
    drawEasy()

    goto(0, -200)
    setheading(90)
    pencolor("black")
    drawTree(80, angle)

    goto(200, 0)
    setheading(0)
    drawSquareSpiral(100, 50, 18)


#pede valor novo para abertura da arvore
novoAngulo = numinput("Árvore", "Digite o ângulo (10 a 60):", 25, 10, 60)

if novoAngulo:
    pu()
    atualizarArvore(novoAngulo)

done()