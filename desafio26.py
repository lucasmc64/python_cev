print('{} DESAFIO 26 {}'.format('=' * 10, '=' * 10))
fr = str(input('Digite uma frase: ')).strip().lower()
#Quantas vezes aparece a letra 'a'
print('A letra A aparece {} vezes nessa frase!'.format(fr.count('a')))
#Em que posição aparece a primeira vez
print('A letra A aparece pela primeira vem a posição {}!'.format(fr.find('a') + 1))
#Em que posição ela aparece a última vez
print('A última letra A aparece na posição {}!'.format(fr.rfind('a') + 1))