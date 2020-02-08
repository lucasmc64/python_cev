print('{} DESAFIO 40 {}'.format('='*10, '='*10))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi de {:.2f}!'.format(m))
if m < 5.0:
    print('\033[31mREPROVADO!\033[m')
elif 5.0 <= m <= 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m')
elif 7.0 <= m:
    print('\033[36mAPROVADO!\033[m')