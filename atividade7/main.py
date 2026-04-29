import random

def jokenpo():
    pontos = 0
    pontosbot = 0
    while True:
    
        escolhas = ['pedra','papel','tesoura']
        escolha = input('Escolha sua jogada (pedra,papel ou tesoura): ')
        escolhabot = random.choice(escolhas)

        print(f'A escolha do bot é: {escolhabot}')

        if escolha == escolhabot:
            print('------EMPATE-----')
        elif escolha == 'papel' and escolhabot == 'pedra' or \
        escolha == 'pedra' and escolhabot == 'tesoura' or \
        escolha == 'tesoura' and escolhabot == 'papel':
            print('----VOCÊ GANHOU!-----')
            pontos += 1
        else:
            print('-----VOCÊ PERDEU!-----')
            pontosbot += 1
        print('=' * 50)
        print('Pontuaçao final:')
        print(f'pontos bot: {pontosbot}')
        print(f'pontos usuario: {pontos}')
        print('=' * 50)
        continuar = input('quer continuar? ')
        if continuar == 'sim':
            print('Continuando...')
        else:
            break 

jokenpo()