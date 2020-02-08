from math import hypot
print('{} DESAFIO 17 {}'.format('='*10, '='*10))
catop = int(input('Digite o valor do cateto oposto do triângulo retângulo: '))
catadj = int(input('Digite o valor do  cateto adjacente do triângulo retângulo: '))
hip = hypot(catop, catadj)
print('O valor da Hipotenusa deste triângulo retângulo é {}!'.format(hip))
#hip2 = math.sqrt(catop ** 2 + catadj ** 2)
#print('O valor da Hipotenusa deste triângulo retângulo é {}!'.format(hip2))
