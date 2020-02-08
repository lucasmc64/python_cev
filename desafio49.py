print('{} DESAFIO 49 {}\n'.format('='*10, '='*10))
n = int(input('Digite um número: '))
print('\n\033[31mTABUADA DO {}\033[m'.format(n))
for c in range(0, 11):
    print('{} X {:2} = {:2}'.format(n, c, n * c))