from random import shuffle
print('{} DESAFIO 20 {}'.format('='*10, '='*10))
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será \n{}'.format(lista))
