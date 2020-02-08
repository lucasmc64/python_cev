print('{} DESAFIO 50 {}\n'.format('='*10, '='*10))
s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if(n % 2 == 0):
        s += n
print('\nA soma dos pares vale: {}.'.format(s))