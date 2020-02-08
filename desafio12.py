print('{} DESAFIO 12 {}'.format('='*10, '='*10))
preco = float(input('Informe o preço do produto: '))
desc = (preco * 5)/100
npreco = preco - desc
print('O preço do produto com 5% de desconto é R${}!'.format(npreco))
