import random

def escolher_palavra():
    palavras = ['pizza', 'hamburguer', 'sushi', 'lasanha', 'estrogonofe']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_descobertas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_descobertas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    return exibicao

def forca():
    while True:
        palavra = escolher_palavra()
        letras_descobertas = []
        vidas = 6

        print('=== JOGO DA FORCA ===')
        print('Tema: Comidas')

        while vidas > 0:
            print(mostrar_palavra(palavra, letras_descobertas))
            print(f'Vidas: {vidas}')

            tentativa = input('Digite uma letra ou palavra: ').lower()

            if not tentativa.isalpha():
                print('Digite apenas letras!')
                continue

            if len(tentativa) > 1:
                if tentativa == palavra:
                    print(f'ACERTOU! A palavra era: {palavra}')
                    break
                else:
                    print('Errou o chute!')
                    vidas -= 1
                    continue

            
            if tentativa in letras_descobertas:
                print('Você já tentou essa letra')
                continue

            letras_descobertas.append(tentativa)

            if tentativa not in palavra:
                vidas -= 1

            if all(letra in letras_descobertas for letra in palavra):
                print(f'VOCÊ GANHOU! Palavra: {palavra}')
                break

        if vidas == 0:
            print(f'PERDEU! Palavra era: {palavra}')

        reiniciar = input('Jogar novamente? (sim/nao): ')
        if reiniciar != 'sim':
            break

forca()