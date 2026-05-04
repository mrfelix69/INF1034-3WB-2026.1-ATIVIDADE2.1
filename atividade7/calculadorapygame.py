import pygame

pygame.init()

# Tela
WIDTH, HEIGHT = 300, 400
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculadora")

# Fonte
font = pygame.font.SysFont(None, 40)

# Cores
BRANCO = (255,255,255)
CINZA = (200,200,200)
PRETO = (0,0,0)

# Variáveis
valor_atual = ''
resultado = None
operador = None

# Botões (texto, posição)
botoes = [
    ('7', 0, 100), ('8', 75, 100), ('9', 150, 100), ('/', 225, 100),
    ('4', 0, 175), ('5', 75, 175), ('6', 150, 175), ('X', 225, 175),
    ('1', 0, 250), ('2', 75, 250), ('3', 150, 250), ('-', 225, 250),
    ('0', 0, 325), ('C', 75, 325), ('=', 150, 325), ('+', 225, 325),
]

def desenhar():
    tela.fill(PRETO)

    # Display
    texto = font.render(valor_atual if valor_atual else '0', True, BRANCO)
    tela.blit(texto, (10, 30))

    # Botões
    for txt, x, y in botoes:
        pygame.draw.rect(tela, CINZA, (x, y, 70, 60))
        t = font.render(txt, True, PRETO)
        tela.blit(t, (x+20, y+15))

    pygame.display.update()

def calcular(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == 'X': return a * b
    if op == '/': return a / b if b != 0 else 0

rodando = True
while rodando:
    desenhar()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            for txt, bx, by in botoes:
                if bx < x < bx+70 and by < y < by+60:

                    if txt.isdigit():
                        valor_atual += txt

                    elif txt in ['+', '-', 'X', '/']:
                        if valor_atual:
                            if resultado is None:
                                resultado = float(valor_atual)
                            else:
                                resultado = calcular(resultado, operador, float(valor_atual))
                            operador = txt
                            valor_atual = ''

                    elif txt == '=':
                        if valor_atual and operador:
                            resultado = calcular(resultado, operador, float(valor_atual))
                            valor_atual = str(resultado)
                            resultado = None
                            operador = None

                    elif txt == 'C':
                        valor_atual = ''
                        resultado = None
                        operador = None

pygame.quit()