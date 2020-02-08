print('{} DESAFIO 22 {}'.format('='*10, '='*10))
n = str(input('Por favor, digite seu nome completo: ')).strip()
#Nome com todas as letras maiúsculas
mai = n.upper()
print('Seu nome em maiúsculas é {}'.format(mai))
#Nome com todas as letras maiúsculas
min = n.lower()
print('Seu nome em maiúsculas é {}'.format(min))
#Quantas letras ao tem sem considerar os espaços
tot = len(n)
spc = n.count(' ')
tletras = tot - spc
print('Seu nome tem ao todo {} letras!'.format(tletras))
#Quantas letras tem o 1º nome
name = n.split()
qt = len(name[0])
print('Seu primeiro nome é {} e tem {} letras'.format(name[0], qt))
