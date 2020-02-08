from datetime import date
print('{} DESAFIO 54 {}'.format('='*10, '='*10))
ano = date.today()
ano = ano.year
c = 0
for i in range(0, 7):
    id = int(input('Digite seu ano de nascimento: '))
    if(ano - id < 21):
        c = c + 1
print('São {} menores de idade'.format(c))
print('São {} maiores de idade'.format(7 - c))
