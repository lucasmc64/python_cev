print('{} DESAFIO 6 {}'.format('='*10, '='*10))
n = int(input('Digite o número desejado: '))
print('O dobro, triplo e raiz quadrada do número \033[31m{}\033[m é, respectivamente, \033[35m{}\033[m, \033[33m{}\033[m e \033[34m{:.2f}\033[m.'.format(n, n * 2, n * 3, n**(1/2)))