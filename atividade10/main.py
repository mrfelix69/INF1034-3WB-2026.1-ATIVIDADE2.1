import sys
import random
import pygame
from pygame.locals import *

pygame.init()

# INPUT DO USUARIO PARA HISTOGRAMA 3

lista3 = []

print("Digite numeros para o histograma 3")
print("Digite -1 para parar")

while True:

    num = int(input("Digite um numero: "))

    # para quando digitar -1
    if num == -1:
        break

    lista3.append(num)

# caso usuario nao digite nada
if len(lista3) == 0:

    lista3 = [0]

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption("3 Histogramas")

fonte = pygame.font.SysFont(None, 24)
fonte_titulo = pygame.font.SysFont(None, 35)

BRANCO = (255,255,255)
PRETO = (0,0,0)

# HISTOGRAMA 1 (lista aleatorai com 50 numeros)

lista1 = []

# adiciona 50 numeros aleatorios
for i in range(50):

    lista1.append(random.randint(0,200))

# HISTOGRAMA 2 (lista estatica)

lista_estatica = [
    100,120,130,120,150,
    100,160,200,100,110,
    90,80,70,60,50,
    40,30,20,10,5
]

# pega quantidade aleatoria sem ultrapassar lista
quantidade = random.randint(5, len(lista_estatica))

# escolhe elementos aleatorios da lista estatica
lista2 = random.sample(lista_estatica, quantidade)

# menu interativo

histograma_atual = 0

# funcao para gerar uma cor aleatoria

def gerarcor():

    return (
        random.randint(50,255),
        random.randint(50,255),
        random.randint(50,255)
    )

cores1 = [gerarcor() for _ in range(5)]
cores2 = [gerarcor() for _ in range(6)]
cores3 = [gerarcor() for _ in range(4)]

# funcao para categorias serem contabilizada

def contabilizatot(nums, num_cat):

    # menor numero
    num_min = min(nums)

    # maior numero
    num_max = max(nums)

    # tamanho de cada categoria
    tam_cat = (num_max - num_min + 1) / num_cat

    # lista zerada
    lista_total = [0] * num_cat

    # percorre numeros
    for i in range(len(nums)):

        # caso seja ultimo numero
        if nums[i] == num_max:

            lista_total[-1] += 1

            continue

        # percorre categorias
        for i_cat in range(num_cat):

            # limite inferior
            lim_inf = num_min + i_cat * tam_cat

            # limite superior
            lim_sup = lim_inf + tam_cat

            # verifica categoria correta
            if lim_inf <= nums[i] < lim_sup:

                lista_total[i_cat] += 1

                break

    return lista_total, num_min, tam_cat

# funcao para desenhar o histograma

def drawhistograma(screen, nums, num_cat, pos_x, titulo, cores):

    # pega altura da tela
    screen_h = screen.get_height()

    # contabiliza categorias
    lista_total, num_min, tam_cat = contabilizatot(nums, num_cat)

    # maior valor
    maior = max(lista_total)

    # desenha titulo
    texto = fonte_titulo.render(titulo, True, PRETO)

    screen.blit(texto, (pos_x + 30, 80))

    
    # desenho dos eixos
    

    # eixo X
    pygame.draw.line(
        screen,
        PRETO,
        (pos_x, 600),
        (pos_x + 300, 600),
        3
    )

    # eixo Y
    pygame.draw.line(
        screen,
        PRETO,
        (pos_x, 250),
        (pos_x, 600),
        3
    )

    # desenho das barra

    for i in range(len(lista_total)):

        # posicao X
        x = pos_x + 20 + i * 50

        if maior == 0:

            h = 0

        else:

            # altura da barra
            h = (lista_total[i] / maior) * 250

        cor = cores[i]

        # desenha barra
        pygame.draw.rect(
            screen,
            cor,
            (x, screen_h - 100 - h, 30, h)
        )

       
        # texto X
        

        faixa = int(num_min + i * tam_cat)

        texto_x = fonte.render(str(faixa), True, PRETO)

        screen.blit(texto_x, (x, 610))

        
        # texto Y
        

        texto_y = fonte.render(
            str(lista_total[i]),
            True,
            PRETO
        )

        screen.blit(
            texto_y,
            (x, screen_h - 120 - h)
        )

# loop principal

while True:

   
    # eventos
    

    for event in pygame.event.get():

        # fechar tela
        if event.type == QUIT:

            pygame.quit()

            sys.exit()

        if event.type == KEYDOWN:

            # seta direita
            if event.key == K_RIGHT:

                histograma_atual += 1

                if histograma_atual > 2:

                    histograma_atual = 0

            # seta esquerda
            if event.key == K_LEFT:

                histograma_atual -= 1

                if histograma_atual < 0:

                    histograma_atual = 2

    screen.fill(BRANCO)

    # mensagem do menu

    texto_menu = fonte.render(
        "Clique SETA DIREITA ou ESQUERDA para trocar de histograma",
        True,
        PRETO
    )

    screen.blit(texto_menu, (300,20))

    # HISTOGRAMA 1 com 5 categorias

    if histograma_atual == 0:

        drawhistograma(
            screen,
            lista1,
            5,
            400,
            "Histograma Aleatorio",
            cores1
        )

    # HISTOGRAMA 2 com 6 categorias

    elif histograma_atual == 1:

        drawhistograma(
            screen,
            lista2,
            6,
            400,
            "Histograma Estatico",
            cores2
        )

    # HISTOGRAMA 3 com 4 categorias

    elif histograma_atual == 2:

        drawhistograma(
            screen,
            lista3,
            4,
            400,
            "Histograma Usuario",
            cores3
        )

    pygame.display.update()