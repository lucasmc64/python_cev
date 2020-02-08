import random
print('{} DESAFIO 19 {}'.format('='*10, '='*10))
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
print('O aluno(a) escolhido para apagar o quadro hoje foi {}!'.format(random.choice(lista)))
