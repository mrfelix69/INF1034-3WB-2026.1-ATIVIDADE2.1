import pygame

#função que valida se o email, ele possui o que foi pedido no caso o @puc.com, analisando da 8 letra a diante, até acabar a string/email, caso o email possua o '@puc.com'
#ela retornara 'True', caso ao contrario, ela retornara 'False'
def valida_email(email):

    return email[-8:] == '@puc.com'

#função criada para verificar se a senha possui alguma letra Maiuscula, a função verifica durante toda a senha se possui alguma letra em maiusculo, caso tenha
#ela retornará 'True', porém se ao verificar toda a senha e não encontrar algum palavra em maiusculo ela retornara 'False'.
def possuimaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': #letra.isupper
            return True
    return False

#função criada para verificar se a senha possui alguma letra Minuscula, a função funciona do mesmo modo que a 'Maiuscula' porém, verificando as letras minusculas
#ao verificar toda a senha, toda a string, caso tenha uma letra minuscula ela irá retornar 'True', caso ao contrario ela retornara 'False'.
def possuiminuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': #letra.islower
            return True
    return False

#função criada para verificar se a senha possui número, bem parecida com as anteriores, ela verifica se na senha possui algum caracter entre (0 a 9), retornando True
#se tiver número na senha, verificando a senha toda até achar algum número, caso a função não encontre esse caracter, ela retornará 'False'.
def possuinumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False


#função valida senha ela tem como obejtivo validar a senha checando atráves da junção das outras funçoes se a senha ela é valida ou não, assim no final retornando
#todos os checks com todos dando 'True', se somente 1 der 'False' a senha será invalida

def valida_senha(senha):
    check_tamanho = len(senha) >=8
    check_minuscula = possuiminuscula(senha)
    check_maiuscula = possuimaiuscula(senha)
    check_numero = possuinumero(senha)
    return check_tamanho and check_minuscula and check_maiuscula and check_numero

def criptografasenha(senha):
    senha_crip = ''
    for carac in senha:
        if carac.isdigit():
            #copiar logica do maiusculo, trocando ref para 'a'
            ref = ord('0') #A = 65
            ascii_carac = ord(carac) #1 etapa
            pos_alfa = ascii_carac - ref #2 etapa ()
            pos_ces = pos_alfa + 3 #3 etapa (pega a posição da letra do alfabeto e soma 3, como por exemplo a letra 'A' = 65, se for ela soma 3, resultando em 68, obtendo uma nova letra)
            pos_rest = pos_ces%10 #4 etapa (divide o numero pelo tanto de letras do alfabeto (26 letras) e obtem o resto da divisao).
            letra_ces = chr(ref+pos_rest) #5 etapa ()
            senha_crip += letra_ces
            pass
        elif 'A' <= carac <= 'Z':
            ref = ord('A') #A = 65
            ascii_carac = ord(carac) #1 etapa
            pos_alfa = ascii_carac - ref #2 etapa ()
            pos_ces = pos_alfa + 3 #3 etapa (pega a posição da letra do alfabeto e soma 3, como por exemplo a letra 'A' = 65, se for ela soma 3, resultando em 68, obtendo uma nova letra)
            pos_rest = pos_ces%26 #4 etapa (divide o numero pelo tanto de letras do alfabeto (26 letras) e obtem o resto da divisao).
            letra_ces = chr(ref+pos_rest) #5 etapa ()
            senha_crip += letra_ces
            
        elif 'a' <= carac <= 'z':
            ref = ord('a') #A = 65
            ascii_carac = ord(carac) #1 etapa
            pos_alfa = ascii_carac - ref #2 etapa ()
            pos_ces = pos_alfa + 3 #3 etapa (pega a posição da letra do alfabeto e soma 3, como por exemplo a letra 'A' = 65, se for ela soma 3, resultando em 68, obtendo uma nova letra)
            pos_rest = pos_ces%26 #4 etapa (divide o numero pelo tanto de letras do alfabeto (26 letras) e obtem o resto da divisao).
            letra_ces = chr(ref+pos_rest) #5 etapa ()
            senha_crip += letra_ces
            pass
        else:
            senha_crip += carac
    return senha_crip

print(criptografasenha('ZARALHAR'))

# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# running = True

# pygame.display.update()