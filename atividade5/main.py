from pygame import *
import sys

init()

# (variable) batman_png surface 
batman_font = font.Font('batmfa__.ttf', 26)
batman_img = image.load('pngegg.png')
batman_ing = transform.scale(batman_img,(165,165))
mixer.init()
mixer.music.load('batman_1966.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(0)

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
    draw.polygon(window,(0,255,0),((350,300),(600,300),(475,200))) #telhado
    draw.rect(window,(255, 255, 255),(350,300,250,250),0) #casa
    draw.rect(window,(121, 77, 27),(495,390,80,160),0) #porta
    draw.circle(window,(0,0,0),(510,485),8)
    draw.rect(window,(107, 73, 34),(900,400,40,150),0) #tronco
    draw.circle(window,(232, 118, 205),(920,350,),90) #arvore
    draw.rect(window,(97, 97, 97),(380,410,75,75),0) #janela
    draw.rect(window,(0,0,0),(380,410,75,75),3) #janela

    draw.line(window,(255,242,81),(200,50),(200,90),6)
    draw.line(window,(255,242,81),(200,210),(200,250),6)
    draw.line(window,(255,242,81),(100,150),(140,150),6)
    draw.line(window,(255,242,81),(260,150),(300,150),6)
    draw.line(window,(255,242,81),(120,70),(170,120),6)
    draw.line(window,(255,242,81),(280,70),(230,120),6)
    draw.line(window,(255,242,81),(120,230),(170,180),6)
    draw.line(window,(255,242,81),(280,230),(230,180),6)

    draw.circle(window,(255,255,255),(900,120),50) #nuvem
    draw.circle(window,(255,255,255),(950,120),50) #nuvem
    draw.circle(window,(255,255,255),(850,120),50) #nuvem   
    draw.circle(window,(255,255,255),(1000,120),50) #nuvem 

    draw.line(window, (255,255,255), (417, 410), (417, 485), 3)#janela2
    draw.line(window, (255,255,255), (380, 447), (455, 447), 3)#janela2

    draw.circle(window,(255,0,0),(900,350),10)   # maçã
    draw.circle(window,(255,165,0),(970,330),10) # laranja
    draw.circle(window,(255,0,0),(880,310),10)
    draw.circle(window,(255,165,0),(940,380),10)

    draw.line(window,(101,67,33),(900,340),(900,330),2)
    draw.line(window,(101,67,33),(970,320),(970,310),2)
    draw.line(window,(101,67,33),(880,300),(880,290),2)
    draw.line(window,(101,67,33),(940,370),(940,360),2)

    batman_text1 = batman_font.render('A',True,(0,0,0))
    batman_text2 = batman_font.render('BatCaverna',True,(0,0,0))

    window.blit(batman_ing,(600,390))
    window.blit(batman_text1,(680,300))
    window.blit(batman_text2,(620,350))


    display.update()