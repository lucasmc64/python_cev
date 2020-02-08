print('{} DESAFIO 52 {}\n'.format('='*10, '='*10))
n = int(input('Digite um numero: '))
c = 0
for i in range(1, n + 1):
    if(n % i == 0):
        c = c + 1;
        print('\033[32m{}\033[m'.format(i), end= ' ')
    else:
        print('\033[31m{}\033[m'.format(i), end= ' ')
if(c == 2):
    print('\033[36mÉ UM NÚMERO PRIMO!\033[m')
else:
    print('\033[32mNÃO É NÚMERO PRIMO!\033[m')
