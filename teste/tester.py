import pygame

pygame.init()
print("Pygame instalado com sucesso!")

from pygame import *
import sys

init()

# (variable) batman_png surface
# batman_ing = image.load('bataura')
# batman_ing = transform.scale(batman_png,(200,200))

window = display.set_mode((1200,700))

window.fill((151, 209, 250))

while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    #desenho

    # draw.rect(window,(255,0,0),(200,300,100,50),0)

    draw.circle(window,(255,242,81),(200,150),70) #sol
    draw.rect(window,(72, 157, 37),(0,550,1200,700),0) #grama
    draw.polygon(window,(0,255,0),((350,500),(300,450),(250,400))) #telhado
    draw.rect(window,(255, 255, 255),(350,300,250,250),0) #casa
    draw.rect(window,(121, 77, 27),(495,420,80,130),0) #porta
    draw.circle(window,(0,0,0),(510,485),8)
    draw.rect(window,(107, 73, 34),(900,400,40,150),0) #tronco
    draw.line(window,(255, 242, 81),(100,100),(200,200),4) #raio sol
    draw.circle(window,(232, 118, 205),(920,350,),90) #arvore

    #batman
    # batman_text = batman_font.render('I am batman',True,(0,0,0))
    # window.blit(batman_ing,(0,0))

    display.update()