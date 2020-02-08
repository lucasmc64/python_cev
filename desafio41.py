from datetime import date
print('{} DESAFIO 41 {}'.format('='*10, '='*10))
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria MIRIM!')
elif 9 < idade <= 14:
    print('Categoria INFANTIL!')
elif 14 < idade <= 19:
    print('Categoria JUNIOR!')
elif 19 < idade <= 25:
    print('Categoria SÊNIOR!')
elif 25 < idade:
    print('Categoria MASTER!')