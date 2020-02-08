from random import randint
print('{} DESAFIO 28 {}'.format('='*10, '='*10))
aleat = randint(0, 5)
n = int(input("""Hey, hey, hey! Para meu jogo vencer, advinhe que número de 0 a 5 pensei!"""))
if n == aleat:
    print('ACERTOU MIZARÁVI! VOCÊ VENCEU!')
else:
    print('ERROOW BIXOO! ERA {}!'.format(aleat))