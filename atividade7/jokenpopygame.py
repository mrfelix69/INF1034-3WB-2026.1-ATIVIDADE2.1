import random
import pygame

pygame.init()
tela = pygame.display.set_mode((500,400))
pygame.display.set_caption('Jokenpo')

font = pygame.font.SysFont(None, 40)
escolhas = ['pedra', 'papel', 'tesoura']
resultado = ''

def desenhar(texto):
    tela.fill((0,0,0))
    txt = font.render(texto, True, (255,255,255))
    tela.blit(txt, (50,150))
    pygame.display.update()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                jogador = 'pedra'
            elif event.key == pygame.K_2:
                jogador = 'papel'
            elif event.key == pygame.K_3:
                jogador = 'tesoura'
            else:
                continue

            bot = random.choice(escolhas)

            if jogador == bot:
                resultado = 'Empate'
            elif (jogador == 'pedra' and bot == 'tesoura') or \
                 (jogador == 'papel' and bot == 'pedra') or \
                 (jogador == 'tesoura' and bot == 'papel'):
                resultado = 'Voce ganhou'
            else:
                resultado = 'Voce perdeu'

            desenhar(f'{jogador} x {bot} = {resultado}')

pygame.quit()