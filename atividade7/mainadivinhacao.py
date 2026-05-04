import random

def usuario_adivinha():
    numero = random.randint(1, 1023)
    tentativas = 0

    while True:
        chute = int(input('Digite um número entre 1 e 1023: '))
        tentativas += 1

        if chute > numero:
            print(-1)
        elif chute < numero:
            print(1)
        else:
            print(0)
            print(f'Acertou em {tentativas} tentativas!')
            break

def computador_adivinha():
    print('Pense em um número entre 1 e 1023...')

    baixo = 1
    alto = 1023
    tentativas = 0

    while True:
        chute = (baixo + alto) // 2
        tentativas += 1

        print(f'Computador chuta: {chute}')
        resposta = int(input('Digite -1 (menor), 1 (maior), 0 (igual): '))

        if resposta == 0:
            print(f'Computador acertou em {tentativas} tentativas!')
            break
        elif resposta == -1:
            alto = chute - 1
        elif resposta == 1:
            baixo = chute + 1

def jogo_adivinhacao():
    while True:
        modo = input('Quem vai adivinhar? (usuario/computador)\n' \
        'quando (-1) o chute está alto; (1) o chute está baixo; (0) o chute está certo: ').lower()

        if modo == 'usuario':
            usuario_adivinha()
        elif modo == 'computador':
            computador_adivinha()
        else:
            print('Escolha inválida')
            continue

        repetir = input('Jogar novamente? (sim/nao): ')
        if repetir != 'sim':
            break

jogo_adivinhacao()