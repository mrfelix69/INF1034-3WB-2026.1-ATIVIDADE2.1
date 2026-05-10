from pygame import *
import random

init()

window = display.set_mode((1200, 700))
display.set_caption("Jogo da Forca")

fonte = font.SysFont(None, 40)
fonte_pequena = font.SysFont(None, 30)
fonte_grande = font.SysFont(None, 60)

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

    palavras = [
        'hamburguer',
        'sushi',
        'pizza',
        'feijoada',
        'arroz',
        'carne',
        'lasanha'
    ]

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

            vidas_txt = fonte.render(
                f'Vidas restantes: {vidas}',
                True,
                (255,0,0)
            )

            letras_txt = fonte.render(
                f'Letras usadas: {" ".join(letras)}',
                True,
                (0,0,0)
            )

            info = fonte_pequena.render(
                "Pressione ESC para voltar ao menu",
                True,
                (0,0,0)
            )

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

                        if letra not in letras:

                            letras.append(letra)

                            if letra not in palavra:
                                vidas -= 1

        # TELA FINAL
        esperando = True

        while esperando:

            window.fill((20,20,20))

            if venceu:
                texto = fonte_grande.render(
                    "VOCE VENCEU!",
                    True,
                    (0,255,0)
                )
            else:
                texto = fonte_grande.render(
                    f'VOCE PERDEU! Palavra: {palavra}',
                    True,
                    (255,0,0)
                )

            info1 = fonte.render(
                "ENTER para jogar novamente",
                True,
                (255,255,255)
            )

            info2 = fonte.render(
                "ESC para sair",
                True,
                (255,255,255)
            )

            window.blit(texto, (220,250))
            window.blit(info1, (320,400))
            window.blit(info2, (320,470))

            display.update()

            for ev in event.get():

                if ev.type == QUIT:
                    quit()

                if ev.type == KEYDOWN:

                    if ev.key == K_RETURN:
                        esperando = False

                    if ev.key == K_ESCAPE:
                        quit()

jogo_forca()