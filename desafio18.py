from math import sin, cos, tan, radians
print('{} DESAFIO 18 {}'.format('='*10, '='*10))
ang = int(input('Digite o valor do ângulo em graus (º): '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Para {}º o seno vale {:.2f}, o cosseno {:.2f} e a tangente {:.2f}!'.format(ang, sen, cos, tan))