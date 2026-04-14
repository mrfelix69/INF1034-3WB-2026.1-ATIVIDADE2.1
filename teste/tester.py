from pygame import *

init()

# (variable) batman_png surface 
spiderman_font = font.Font('spiderfont.ttf', 26)
spiderman_img = image.load('spider.png')
spiderman_img = transform.scale(spiderman_img,(250,250))

manha_sfx = mixer.Sound('manha.wav')
tarde_sfx = mixer.Sound('tarde.wav')
noite_sfx = mixer.Sound('noite.wav')
manha_sfx.set_volume(0.3)
tarde_sfx.set_volume(0.3)
noite_sfx.set_volume(0.3)

running = True
clock = time.Clock()


window = display.set_mode((1200,700))

#window.fill((151, 209, 250))

timer = 0
#definicao variaveis
sol_x = 200
sol_y = 150
sol_speed = 300

nuvem_x = 850
nuvem_v = 150
nuvem_min = 100
nuvem_max = 1050
background_color = "#97d1fa"

cor_manha = (135, 206, 250)
cor_tarde = (252, 184, 72)
cor_noite = (15, 24, 82)

def interpolar_cor(cor1, cor2, t):
    t = max(0.0, min(1.0, t))
    return (
        int(cor1[0] + (cor2[0] - cor1[0]) * t),
        int(cor1[1] + (cor2[1] - cor1[1]) * t),
        int(cor1[2] + (cor2[2] - cor1[2]) * t),
    )


def calcular_cor_fundo(sol_x):
    min_x = 70
    max_x = 1130
    pos_normalizada = (sol_x - min_x) / (max_x - min_x)
    pos_normalizada = max(0.0, min(1.0, pos_normalizada))

    if pos_normalizada < 0.5:
        return interpolar_cor(cor_manha, cor_tarde, pos_normalizada * 2)
    return interpolar_cor(cor_tarde, cor_noite, (pos_normalizada - 0.5) * 2)

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                texto = 'I said I AM SPIDER-MAN'
            elif ev.button == 1:
                texto = 'i am spider-man'
        if ev.type == MOUSEMOTION:
            sol_x, sol_y = ev.pos

        if ev.type == KEYDOWN:
            key_pressed = ev.key
            if key_pressed == K_SPACE:
                sol_x = sol_x + 450
                sol_y = sol_y - 150

        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                if sol_x < 400:
                    manha_sfx.play()
                elif sol_x < 800:
                    tarde_sfx.play()
                else:
                    noite_sfx.play()
#update
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    #se eu pressionar a tecla D então sol ir baixo cima esquerda essa coisa

    if keys[K_d]: 
        sol_x += sol_speed * dt
    if keys[K_a]:
        sol_x -= sol_speed * dt
    if keys[K_w]:
        sol_y -= sol_speed * dt
    if keys[K_s]:
        sol_y += sol_speed * dt

    #o sol dentro da janela
    sol_x = max(70, min(1130, sol_x))
    sol_y = max(70, min(630, sol_y))

    nuvem_x += nuvem_v * dt
    if nuvem_x > nuvem_max:
        nuvem_x = nuvem_max
        nuvem_v = -nuvem_v
    elif nuvem_x < nuvem_min:
        nuvem_x = nuvem_min
        nuvem_v = -nuvem_v

    background_color = calcular_cor_fundo(sol_x)

    #desenho
    window.fill(background_color)

    # draw.rect(window,(255,0,0),(200,300,100,50),0)

    draw.circle(window,(255,242,81),(sol_x,sol_y),70) #sol
    draw.rect(window,(72, 157, 37),(0,550,1200,700),0) #grama
    draw.polygon(window,(0,255,0),((350,300),(600,300),(475,200))) #telhado
    draw.rect(window,(255, 255, 255),(350,300,250,250),0) #casa
    draw.rect(window,(121, 77, 27),(495,390,80,160),0) #porta
    draw.circle(window,(0,0,0),(510,485),8)
    draw.rect(window,(107, 73, 34),(900,400,40,150),0) #tronco
    draw.circle(window,(232, 118, 205),(920,350,),90) #arvore
    draw.rect(window,(97, 97, 97),(380,410,75,75),0) #janela
    draw.rect(window,(0,0,0),(380,410,75,75),3) #janela

    draw.line(window,(255,242,81),(sol_x, sol_y-100),(sol_x, sol_y-50),6) #sol
    draw.line(window,(255,242,81),(sol_x, sol_y+100),(sol_x, sol_y+50),6) #sol
    draw.line(window,(255,242,81),(sol_x-100, sol_y),(sol_x-50, sol_y),6) #sol
    draw.line(window,(255,242,81),(sol_x+100, sol_y),(sol_x+50, sol_y),6) #sol
    draw.line(window,(255,242,81),(sol_x-80, sol_y-80),(sol_x-45, sol_y-45),6) #sol
    draw.line(window,(255,242,81),(sol_x+80, sol_y-80),(sol_x+45, sol_y-45),6) #sol
    draw.line(window,(255,242,81),(sol_x-80, sol_y+80),(sol_x-45, sol_y+45),6) #sol
    draw.line(window,(255,242,81),(sol_x+80, sol_y+80),(sol_x+45, sol_y+45),6) #sol

    #nuvens

    draw.circle(window,(255,255,255),(nuvem_x,120),50) #nuvem
    draw.circle(window,(255,255,255),(nuvem_x+50,120),50) #nuvem
    draw.circle(window,(255,255,255),(nuvem_x-50,120),50) #nuvem   
    draw.circle(window,(255,255,255),(nuvem_x+100,120),50) #nuvem 

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

    spiderman1 = spiderman_font.render('I Am',True,(0,0,0))
    spiderman2 = spiderman_font.render('Spider-Man',True,(0,0,0))

    window.blit(spiderman_img,(600,390))
    window.blit(spiderman1,(680,300))
    window.blit(spiderman2,(620,350))




    display.update()