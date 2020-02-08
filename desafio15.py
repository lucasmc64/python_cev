print('{} DESAFIO 15 {}'.format('='*10, '='*10))
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos kilômetros foram rodados? '))
pdias = dias * 60
pkm = km * 0.15
print('O total a pagar é de R${:.2f}!'.format(pdias + pkm))
