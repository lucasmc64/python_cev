print('{} DESAFIO 35 {}'.format('='*10, '='*10))
r1 = float(input('Digite o valor da 1ª reta: '))
r2 = float(input('Digite o valor da 2ª reta: '))
r3 = float(input('Digite o valor da 3ª reta: '))
if abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r2 - r1) < r3 < r2 + r1:
    print('Essas retas PODEM formar um triângulo!')
else:
    print('Sorry, NÃO deu pra formar um triângulo!')