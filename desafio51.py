print('{} DESAFIO 51 {}\n'.format('='*10, '='*10))
primeiro = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for c in range(0, 10):
    if(c == 0):
        print('{}'.format(primeiro), end=' ')
    else:
        primeiro += r
        print('{}'.format(primeiro), end= ' ')