print('{} DESAFIO 34 {}'.format('='*10, '='*10))
sal = float(input('Digite o valor do salário: R$'))
if sal <= 1250:
    print('O salário com aumento de 15% passa a ser R${:.2f}!'.format(sal + ((sal * 15) / 100)))
else:
    print('O salário com aumento de 10% passa a ser R%{:.2f}!'.format(sal + ((sal * 10) / 100)))