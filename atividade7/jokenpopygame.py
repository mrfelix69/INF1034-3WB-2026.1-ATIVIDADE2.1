import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jokenpô com Imagens")

font = pygame.font.SysFont(None, 40)

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

def decidir_vencedor(j, b):
    if j == b:
        return "Empate"
    elif (j == 'pedra' and b == 'tesoura') or \
         (j == 'papel' and b == 'pedra') or \
         (j == 'tesoura' and b == 'papel'):
        return "Você ganhou"
    else:
        return "Você perdeu"

def desenhar():
    tela.fill((30, 30, 30))

    titulo = font.render("Escolha sua jogada", True, (255,255,255))
    tela.blit(titulo, (180, 20))

    tela.blit(pedra_img, (50, 200))
    tela.blit(papel_img, (240, 200))
    tela.blit(tesoura_img, (430, 200))

    #resultado
    if resultado:
        txt = font.render(resultado, True, (255,255,0))
        tela.blit(txt, (200, 100))

    #escolhasfeitas
    if jogador:
        tela.blit(imagens[jogador], (100, 120))
    if bot:
        tela.blit(imagens[bot], (380, 120))

    pygame.display.update()

rodando = True
while rodando:
    desenhar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if 50 < x < 170 and 200 < y < 320:
                jogador = 'pedra'
            elif 240 < x < 360 and 200 < y < 320:
                jogador = 'papel'
            elif 430 < x < 550 and 200 < y < 320:
                jogador = 'tesoura'
            else:
                continue

            bot = random.choice(escolhas)
            resultado = decidir_vencedor(jogador, bot)

pygame.quit()