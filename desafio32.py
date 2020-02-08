from datetime import date
print('{} DESAFIO 32 {}'.format('='*10, '='*10))
ano = int(input('Digite um ano qualquer (Ou 0 se quiser a análise do ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano != 100 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))