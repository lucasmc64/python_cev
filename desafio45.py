from time import sleep
from random import choice
print('\033[30m{} DESAFIO 45 {}\033[m\n'.format('='*10, '='*10))
sleep(1)
print('\033[31m-\033[30m=\033[m'*5, end='')
sleep(1)
print(' \033[36mJO\033[31m-\033[m', end='')
sleep(1)
print('\033[35mKEN\033[31m-\033[m', end='')
sleep(1)
print('\033[33mPÔ\033[30m!\033[m ', end='')
sleep(1)
print('\033[30m=\033[31m-\033[m'*5)
sleep(1)
lista = ['Pedra', 'Papel', 'Tesoura']
resp = str(input('\nTente ganhar do computador! \nEscolha: pedra, papel ou tesoura?\n')).strip().title()
comp = choice(lista)
print(comp)
if comp == resp:
    print('\033[33mHouve um EMPATE! Hahaha, tente de novo!\033[m')
elif comp != resp:
    if comp == 'Pedra' and resp == 'Tesoura':
        print('\033[31mVocê PERDEU! Tente novamente!\033[m')
    elif comp == 'Tesoura' and resp == 'Papel':
        print('\033[31mVocê PERDEU! Tente novamente!\033[m')
    elif comp == 'Papel' and resp == 'Pedra':
        print('\033[31mVocê PERDEU! Tente novamente!\033[m')
    elif resp == 'Pedra' and comp == 'Tesoura':
        print('\033[36mVocê GANHOU! Meus parabéns!\033[m')
    elif resp == 'Tesoura' and comp == 'Papel':
        print('\033[36mVocê GANHOU! Meus parabéns!\033[m')
    elif resp == 'Papel' and comp == 'Pedra':
        print('\033[36mVocê GANHOU! Meus parabéns!\033[m')
    else:
        print('\033[31mERRO! Reinicie o programa e tente novamente!\033[m')
