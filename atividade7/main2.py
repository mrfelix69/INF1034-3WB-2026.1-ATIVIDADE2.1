import math

def calculadora():
    
    print('Operadores disponiveis: ')
    print('=' * 30)
    print('+ adição')
    print('- subtração')
    print('X multiplicação')
    print('/ divisão')
    print('=' * 30)

    a = float(input('Insira o valor de a: '))
    operador = input('Insira o operador desejado: ')
    b = float(input('Insira o valor de b: '))

    if operador == '+':
        resultado = a+b
        print(f'{a} + {b} = {resultado}')
    elif operador == '-':
        resultado = a-b
        print(f'{a} - {b} = {resultado}')
    elif operador == 'X':
        resultado = a*b
        print(f'{a} X {b} = {resultado}')
    elif operador == '/':
        resultado = a/b
        print(f'{a} / {b} = {resultado}')
    else:
        print('Operação inválida')

    while True:

        entrada = input('Deseja continuar com essa operação? (sim/nao): ')

        if entrada != 'sim':
            print('Ok')
            resultado = a = float(input('Insira o valor de a: '))
            
        print('Operadores disponiveis: ')
        print('=' * 30)
        print('+ adição')
        print('- subtração')
        print('X multiplicação')
        print('/ divisão')
        print('=' * 30)

        novooperador = input('Insira o novo operador desejado: ')
        c = float(input('Insira o novo valor: '))
        
        ultimaoperacao = resultado

        if novooperador == '+':
            resultado = ultimaoperacao + c
            print(f'{ultimaoperacao} + {c} = {resultado}')
        elif novooperador == '-':
            resultado = ultimaoperacao - c
            print(f'{ultimaoperacao} - {c} = {resultado}')
        elif novooperador == 'X':
            resultado = ultimaoperacao * c
            print(f'{ultimaoperacao} X {c} = {resultado}')
        elif novooperador == '/':
            resultado = ultimaoperacao/c
            print(f'{ultimaoperacao} / {c} = {resultado}')
        else:
            print('Operação inválida')

calculadora()