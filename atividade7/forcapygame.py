import pygame
import random

pygame.init()

tela = pygame.display.set_mode((600, 400))
font = pygame.font.SysFont(None, 40)

palavras = ['hamburguer','sushi','pizza','feijoada','arroz','carne','lasanha']
palavra = random.choice(palavras)

letras = []
vidas = 6
texto = ''

def desenhar():
    tela.fill((0,0,0))

    exibicao = ''
    for l in palavra:
        exibicao += l + ' ' if l in letras else '_ '

    txt = font.render(exibicao, True, (255,255,255))
    tela.blit(txt, (50, 200))

    vidas_txt = font.render(f'Vidas: {vidas}', True, (255,0,0))
    tela.blit(vidas_txt, (50,50))

    pygame.display.update()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            letra = event.unicode.lower()
            if letra.isalpha():
                if letra not in palavra:
                    vidas -= 1
                letras.append(letra)

    desenhar()

pygame.quit()