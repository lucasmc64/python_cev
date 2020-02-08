print('{} DESAFIO 29 {}'.format('='*10, '='*10))
vel = float(input('Digite a velocidade do caro (Km/h): '))
if vel <= 80.0:
    print('Você está dentro do limite!')
else:
    dif = vel - 80
    print('Você ultrapassou o limite!\nTerá de paga uma multa de R$7,00 para cada Km rodado, no total será R${:.2f}!'.format(dif * 7))