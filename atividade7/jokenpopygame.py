import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 450
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jokenpo")

font = pygame.font.SysFont(None, 36)

pedra_img = pygame.image.load("pedra.png")
papel_img = pygame.image.load("papel.jpg")
tesoura_img = pygame.image.load("tesoura.png")

pedra_img = pygame.transform.scale(pedra_img, (120, 120))
papel_img = pygame.transform.scale(papel_img, (120, 120))
tesoura_img = pygame.transform.scale(tesoura_img, (120, 120))

imagens = {
    'pedra': pedra_img,
    'papel': papel_img,
    'tesoura': tesoura_img
}

escolhas = ['pedra', 'papel', 'tesoura']

jogador = None
bot = None
resultado = ''

pontos_jogador = 0
pontos_bot = 0

pode_jogar = False  

def decidir_vencedor(j, b):
    if j == b:
        return "Empate"
    elif (j == 'pedra' and b == 'tesoura') or \
         (j == 'papel' and b == 'pedra') or \
         (j == 'tesoura' and b == 'papel'):
        return "Você ganhou"
    else:
        return "Você perdeu"

def desenhar_botao(texto, x, y, w, h):
    pygame.draw.rect(tela, (200,200,200), (x, y, w, h))
    txt = font.render(texto, True, (0,0,0))
    tela.blit(txt, (x + 10, y + 10))

def desenhar():
    tela.fill((30, 30, 30))

    titulo = font.render("Jokenpô", True, (255,255,255))
    tela.blit(titulo, (250, 10))

    placar = font.render(f'Você {pontos_jogador} x {pontos_bot} Bot', True, (255,255,255))
    tela.blit(placar, (180, 50))

    if pode_jogar:
        tela.blit(pedra_img, (50, 250))
        tela.blit(papel_img, (240, 250))
        tela.blit(tesoura_img, (430, 250))
    else:
        aviso = font.render("Clique em CONTINUAR para jogar", True, (255,255,0))
        tela.blit(aviso, (130, 250))

    if resultado:
        txt = font.render(resultado, True, (255,255,0))
        tela.blit(txt, (200, 100))

    if jogador:
        tela.blit(imagens[jogador], (50, 150))
    if bot:
        tela.blit(imagens[bot], (430, 150))

    desenhar_botao("Continuar", 50, 400, 120, 40)
    desenhar_botao("Reiniciar", 200, 400, 120, 40)
    desenhar_botao("Sair", 350, 400, 100, 40)

    pygame.display.update()

rodando = True
while rodando:
    desenhar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if 50 < x < 170 and 400 < y < 440:
                pode_jogar = True
                jogador = None
                bot = None
                resultado = ''

            elif 200 < x < 320 and 400 < y < 440:
                pontos_jogador = 0
                pontos_bot = 0
                jogador = None
                bot = None
                resultado = ''
                pode_jogar = False

            elif 350 < x < 450 and 400 < y < 440:
                rodando = False

            elif pode_jogar:
                if 50 < x < 170 and 250 < y < 370:
                    jogador = 'pedra'
                elif 240 < x < 360 and 250 < y < 370:
                    jogador = 'papel'
                elif 430 < x < 550 and 250 < y < 370:
                    jogador = 'tesoura'
                else:
                    continue

                bot = random.choice(escolhas)
                resultado = decidir_vencedor(jogador, bot)

                if resultado == "Você ganhou":
                    pontos_jogador += 1
                elif resultado == "Você perdeu":
                    pontos_bot += 1

                pode_jogar = False

pygame.quit()