print('{} DESAFIO 47 {}\n'.format('='*10, '='*10))
print('Abaixo estão todos os números pares de 1 à 50: ')
for c in range(1, 51):
    if(c % 2 == 0):
        print('{}'.format(c), end=' ')