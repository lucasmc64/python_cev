print('{} DESAFIO 48 {}\n'.format('='*10, '='*10))
s = 0
for c in range(1, 501):
    if((c % 2 != 0) and (c % 3 == 0)):
        s += c
print('A soma é {}!'.format(s))