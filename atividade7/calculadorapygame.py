import pygame

pygame.init()

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Calculadora')

font = pygame.font.SysFont(None, 40)

texto = ''

def desenhar():
    tela.fill((0,0,0))
    render = font.render(texto, True, (255,255,255))
    tela.blit(render, (20, 130))
    pygame.display.update()

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                try:
                    texto = str(eval(texto))
                except:
                    texto = 'Erro'
            elif event.key == pygame.K_BACKSPACE:
                texto = texto[:-1]
            else:
                texto += event.unicode

    desenhar()

pygame.quit()