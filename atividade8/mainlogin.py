from pygame import *
import random

init()
mixer.init()


window = display.set_mode((1200, 700))
display.set_caption("Login para Jogos")

clock = time.Clock()

fonte = font.SysFont(None, 40)
fonte_pequena = font.SysFont(None, 30)
fonte_grande = font.SysFont(None, 60)

pedra_img = image.load("pedra.png")
papel_img = image.load("papel.jpg")
tesoura_img = image.load("tesoura.png")

pedra_img = transform.scale(pedra_img, (120,120))
papel_img = transform.scale(papel_img, (120,120))
tesoura_img = transform.scale(tesoura_img, (120,120))

spiderman_font = font.Font('spiderfont.ttf', 26)

spiderman_img = image.load('spider.png')
spiderman_img = transform.scale(spiderman_img,(250,250))

manha_sfx = mixer.Sound('manha.wav')
elden_tarde_sfx = mixer.Sound('eldentarde.wav')
outerwild_night_sfx = mixer.Sound('outerwildnight.wav')

manha_sfx.set_volume(0.3)
elden_tarde_sfx.set_volume(0.3)
outerwild_night_sfx.set_volume(0.3)

def valida_email(email):
    return email[-8:] == '@puc.com'

def possuimaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            return True
    return False

def possuiminuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z':
            return True
    return False

def possuinumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False

def valida_senha(senha):

    check_tamanho = len(senha) >= 8
    check_minuscula = possuiminuscula(senha)
    check_maiuscula = possuimaiuscula(senha)
    check_numero = possuinumero(senha)

    return check_tamanho and check_minuscula and check_maiuscula and check_numero

def criptografasenha(senha):

    senha_crip = ''

    for carac in senha:

        if carac.isdigit():

            ref = ord('0')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa + 3
            pos_rest = pos_ces % 10
            letra_ces = chr(ref + pos_rest)

            senha_crip += letra_ces

        elif 'A' <= carac <= 'Z':

            ref = ord('A')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa + 3
            pos_rest = pos_ces % 26
            letra_ces = chr(ref + pos_rest)

            senha_crip += letra_ces

        elif 'a' <= carac <= 'z':

            ref = ord('a')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa + 3
            pos_rest = pos_ces % 26
            letra_ces = chr(ref + pos_rest)

            senha_crip += letra_ces

        else:
            senha_crip += carac

    return senha_crip

def descriptografasenha(senha):

    senha_descrip = ''

    for carac in senha:

        if carac.isdigit():

            ref = ord('0')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa - 3
            pos_rest = pos_ces % 10
            letra_ces = chr(ref + pos_rest)

            senha_descrip += letra_ces

        elif 'A' <= carac <= 'Z':

            ref = ord('A')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa - 3
            pos_rest = pos_ces % 26
            letra_ces = chr(ref + pos_rest)

            senha_descrip += letra_ces

        elif 'a' <= carac <= 'z':

            ref = ord('a')
            ascii_carac = ord(carac)
            pos_alfa = ascii_carac - ref
            pos_ces = pos_alfa - 3
            pos_rest = pos_ces % 26
            letra_ces = chr(ref + pos_rest)

            senha_descrip += letra_ces

        else:
            senha_descrip += carac

    return senha_descrip

def mostrar_cripto(crip, descrip):

    while True:

        window.fill((20,20,20))

        t1 = fonte.render(f'Senha criptografada: {crip}', True, (0,255,0))
        t2 = fonte.render(f'Senha descriptografada: {descrip}', True, (255,255,0))
        t3 = fonte.render('Pressione ENTER para continuar', True, (255,255,255))

        window.blit(t1, (150,250))
        window.blit(t2, (150,320))
        window.blit(t3, (150,420))

        display.update()

        for ev in event.get():

            if ev.type == QUIT:
                quit()

            if ev.type == KEYDOWN:

                if ev.key == K_RETURN:
                    return

def tela_login():

    email = ''
    senha = ''

    digitando_email = True
    erro = ''

    while True:

        window.fill((30,30,30))

        titulo = fonte_grande.render("LOGIN", True, (255,255,255))

        txt_email = fonte.render(f'Email: {email}', True, (255,255,255))
        txt_senha = fonte.render(f'Senha: {senha}', True, (255,255,255))

        info = fonte_pequena.render("TAB troca campo | ENTER confirma", True, (255,255,0))

        erro_txt = fonte_pequena.render(erro, True, (255,0,0))

        window.blit(titulo, (500,80))
        window.blit(txt_email, (200,250))
        window.blit(txt_senha, (200,350))
        window.blit(info, (200,500))
        window.blit(erro_txt, (200,550))

        display.update()

        for ev in event.get():

            if ev.type == QUIT:
                quit()

            if ev.type == KEYDOWN:

                if ev.key == K_TAB:
                    digitando_email = not digitando_email

                elif ev.key == K_BACKSPACE:

                    if digitando_email:
                        email = email[:-1]
                    else:
                        senha = senha[:-1]

                elif ev.key == K_RETURN:

                    if not valida_email(email):
                        erro = "Email invalido"

                    elif not valida_senha(senha):
                        erro = "Senha fraca"

                    else:

                        senha_crip = criptografasenha(senha)
                        senha_descrip = descriptografasenha(senha_crip)

                        mostrar_cripto(senha_crip, senha_descrip)

                        return

                else:

                    if digitando_email:
                        email += ev.unicode
                    else:
                        senha += ev.unicode

def menu():

    while True:

        window.fill((15,15,15))

        titulo = fonte_grande.render("MENU", True, (255,255,255))

        op1 = fonte.render("1 - Casinha", True, (255,255,255))
        op2 = fonte.render("2 - Jokenpo", True, (255,255,255))
        op3 = fonte.render("3 - Forca", True, (255,255,255))
        op4 = fonte.render("ESC - Sair", True, (255,255,255))

        window.blit(titulo, (500,100))
        window.blit(op1, (450,250))
        window.blit(op2, (450,320))
        window.blit(op3, (450,390))
        window.blit(op4, (450,460))

        display.update()

        for ev in event.get():

            if ev.type == QUIT:
                quit()

            if ev.type == KEYDOWN:

                if ev.key == K_1:
                    casinha()

                elif ev.key == K_2:
                    jogo_jokenpo()

                elif ev.key == K_3:
                    jogo_forca()

                elif ev.key == K_ESCAPE:
                    quit()

def jogo_jokenpo():

    escolhas = ['pedra','papel','tesoura']

    imagens = {
        'pedra': pedra_img,
        'papel': papel_img,
        'tesoura': tesoura_img
    }

    jogador = None
    bot = None

    resultado = ''

    pontos_jogador = 0
    pontos_bot = 0

    pode_jogar = False

    def decidir_vencedor(j,b):

        if j == b:
            return "Empate"

        elif (j == 'pedra' and b == 'tesoura') or \
             (j == 'papel' and b == 'pedra') or \
             (j == 'tesoura' and b == 'papel'):

            return "Voce ganhou"

        else:
            return "Voce perdeu"

    while True:

        window.fill((30,30,30))

        titulo = fonte.render("Jokenpo", True, (255,255,255))
        placar = fonte.render(f'Voce {pontos_jogador} x {pontos_bot} Bot', True, (255,255,255))

        window.blit(titulo, (500,20))
        window.blit(placar, (420,80))

        if pode_jogar:

            window.blit(pedra_img, (200,300))
            window.blit(papel_img, (500,300))
            window.blit(tesoura_img, (800,300))

        else:

            aviso = fonte.render("ENTER para jogar novamente", True, (255,255,0))
            window.blit(aviso, (330,250))

        if jogador:
            window.blit(imagens[jogador], (200,150))

        if bot:
            window.blit(imagens[bot], (800,150))

        txt = fonte.render(resultado, True, (255,255,0))
        window.blit(txt, (450,200))

        sair = fonte_pequena.render("Pressione ESC para voltar ao menu", True, (255,0,0))
        window.blit(sair, (20,20))

        display.update()

        for ev in event.get():

            if ev.type == QUIT:
                quit()

            if ev.type == KEYDOWN:

                if ev.key == K_ESCAPE:
                    return

                if ev.key == K_RETURN:

                    pode_jogar = True
                    resultado = ''
                    jogador = None
                    bot = None

            if ev.type == MOUSEBUTTONDOWN and pode_jogar:

                x, y = ev.pos

                if 200 < x < 320 and 300 < y < 420:
                    jogador = 'pedra'

                elif 500 < x < 620 and 300 < y < 420:
                    jogador = 'papel'

                elif 800 < x < 920 and 300 < y < 420:
                    jogador = 'tesoura'

                else:
                    continue

                bot = random.choice(escolhas)

                resultado = decidir_vencedor(jogador, bot)

                if resultado == "Voce ganhou":
                    pontos_jogador += 1

                elif resultado == "Voce perdeu":
                    pontos_bot += 1

                pode_jogar = False

def desenhar_forca(vidas):

    draw.line(window, (0,0,0), (800,500), (950,500), 5)
    draw.line(window, (0,0,0), (875,500), (875,120), 5)
    draw.line(window, (0,0,0), (875,120), (950,120), 5)
    draw.line(window, (0,0,0), (950,120), (950,150), 5)

    if vidas <= 5:
        draw.circle(window, (0,0,0), (950,180), 30, 3)

    if vidas <= 4:
        draw.line(window, (0,0,0), (950,210), (950,320), 3)

    if vidas <= 3:
        draw.line(window, (0,0,0), (950,240), (900,280), 3)

    if vidas <= 2:
        draw.line(window, (0,0,0), (950,240), (1000,280), 3)

    if vidas <= 1:
        draw.line(window, (0,0,0), (950,320), (900,380), 3)

    if vidas <= 0:
        draw.line(window, (0,0,0), (950,320), (1000,380), 3)

def jogo_forca():

    palavras = ['hamburguer','sushi','pizza','feijoada','arroz','carne','lasanha']

    while True:

        palavra = random.choice(palavras)

        letras = []

        vidas = 6

        venceu = False
        perdeu = False

        jogando = True

        while jogando:

            window.fill((180,220,255))

            exibicao = ''

            for l in palavra:

                if l in letras:
                    exibicao += l + ' '
                else:
                    exibicao += '_ '

            txt = fonte_grande.render(exibicao, True, (0,0,0))

            vidas_txt = fonte.render(f'Vidas restantes: {vidas}', True, (255,0,0))

            letras_txt = fonte.render(f'Letras usadas: {" ".join(letras)}', True, (0,0,0))

            info = fonte_pequena.render("Pressione ESC para voltar ao menu", True, (0,0,0))

            window.blit(txt, (120,300))
            window.blit(vidas_txt, (120,100))
            window.blit(letras_txt, (120,160))
            window.blit(info, (20,20))

            desenhar_forca(vidas)

            if '_' not in exibicao:
                venceu = True
                jogando = False

            if vidas <= 0:
                perdeu = True
                jogando = False

            display.update()

            for ev in event.get():

                if ev.type == QUIT:
                    quit()

                if ev.type == KEYDOWN:

                    if ev.key == K_ESCAPE:
                        return

                    letra = ev.unicode.lower()

                    if letra.isalpha():

                        if letra not in palavra:
                            vidas -= 1

                        if letra not in letras:
                            letras.append(letra)

        while True:

            window.fill((20,20,20))

            if venceu:
                texto = fonte_grande.render("VOCE VENCEU!", True, (0,255,0))
            else:
                texto = fonte_grande.render(f'VOCE PERDEU! Palavra: {palavra}', True, (255,0,0))

            info1 = fonte.render("ENTER para jogar novamente", True, (255,255,255))
            info2 = fonte.render("ESC para voltar ao menu", True, (255,255,255))

            window.blit(texto, (220,250))
            window.blit(info1, (320,400))
            window.blit(info2, (320,470))

            display.update()

            voltar = False

            for ev in event.get():

                if ev.type == QUIT:
                    quit()

                if ev.type == KEYDOWN:

                    if ev.key == K_RETURN:
                        voltar = True

                    elif ev.key == K_ESCAPE:
                        return

            if voltar:
                break

def casinha():

    sol_x = 200
    sol_y = 150

    movimentomouse = False

    nuvem_x = 850
    nuvem_v = 150

    while True:

        dt = clock.tick(60)/1000

        for ev in event.get():

            if ev.type == QUIT:
                quit()

            if ev.type == KEYDOWN:

                if ev.key == K_ESCAPE:
                    return

                if ev.key == K_SPACE:
                    sol_x += 450
                    sol_y -= 150

                if ev.key == K_j:
                    movimentomouse = not movimentomouse

            if ev.type == MOUSEBUTTONUP:

                if ev.button == 1:

                    if sol_x < 400:
                        manha_sfx.play()

                    elif sol_x < 800:
                        elden_tarde_sfx.play()

                    else:
                        outerwild_night_sfx.play()

            if movimentomouse and ev.type == MOUSEMOTION:
                sol_x, sol_y = ev.pos

        keys = key.get_pressed()

        if not movimentomouse:

            if keys[K_d]:
                sol_x += 500 * dt

            if keys[K_a]:
                sol_x -= 500 * dt

            if keys[K_w]:
                sol_y -= 500 * dt

            if keys[K_s]:
                sol_y += 500 * dt

        sol_x = max(70, min(1130, sol_x))
        sol_y = max(70, min(630, sol_y))

        nuvem_x += nuvem_v * dt

        if nuvem_x > 1050 or nuvem_x < 100:
            nuvem_v *= -1

        if sol_x < 400:
            background_color = (135,206,250)

        elif sol_x < 800:
            background_color = (252,184,72)

        else:
            background_color = (15,24,82)

        window.fill(background_color)

        draw.rect(window,(72,157,37),(0,550,1200,700))
        draw.polygon(window,(0,255,0),((350,300),(600,300),(475,200)))
        draw.rect(window,(255,255,255),(350,300,250,250))
        draw.rect(window,(121,77,27),(495,390,80,160))

        draw.circle(window,(0,0,0),(510,485),8)

        draw.rect(window,(107,73,34),(900,400,40,150))

        draw.circle(window,(232,118,205),(920,350),90)

        draw.rect(window,(97,97,97),(380,410,75,75))
        draw.rect(window,(0,0,0),(380,410,75,75),3)

        draw.circle(window,(255,242,81),(sol_x,sol_y),70)

        draw.line(window,(255,242,81),(sol_x, sol_y-100),(sol_x, sol_y-50),6)
        draw.line(window,(255,242,81),(sol_x, sol_y+100),(sol_x, sol_y+50),6)
        draw.line(window,(255,242,81),(sol_x-100, sol_y),(sol_x-50, sol_y),6)
        draw.line(window,(255,242,81),(sol_x+100, sol_y),(sol_x+50, sol_y),6)

        draw.line(window,(255,242,81),(sol_x-80, sol_y-80),(sol_x-45, sol_y-45),6)
        draw.line(window,(255,242,81),(sol_x+80, sol_y-80),(sol_x+45, sol_y-45),6)
        draw.line(window,(255,242,81),(sol_x-80, sol_y+80),(sol_x-45, sol_y+45),6)
        draw.line(window,(255,242,81),(sol_x+80, sol_y+80),(sol_x+45, sol_y+45),6)

        draw.circle(window,(255,255,255),(nuvem_x,120),50)
        draw.circle(window,(255,255,255),(nuvem_x+50,120),50)
        draw.circle(window,(255,255,255),(nuvem_x-50,120),50)
        draw.circle(window,(255,255,255),(nuvem_x+100,120),50)

        draw.line(window, (255,255,255), (417, 410), (417, 485), 3)
        draw.line(window, (255,255,255), (380, 447), (455, 447), 3)

        draw.circle(window,(255,0,0),(900,350),10)
        draw.circle(window,(255,165,0),(970,330),10)
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

        info = fonte_pequena.render("Pressione ESC para voltar ao menu", True, (255,255,255))
        window.blit(info, (20,20))

        display.update()

tela_login()
menu()
quit()