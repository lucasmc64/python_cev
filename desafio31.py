print('{} DESAFIO 31 {}'.format('='*10, '='*10))
km = float(input('Digite a distância (em Km) da sua viagem: '))
if km <= 200:
    print('O valor da passagem será de R${}!'.format(km * 0.5))
else:
    print('O valor da passagem será de R${}!'.format(km * 0.45))