from datetime import date
print('{} DESAFIO 39 {}'.format('='*10, '='*10))
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Quem nasceu wm {} tem {} anos em {}.'.format(ano, idade, atual))
if idade < 18:
    print('Você ainda terá de se listar ao serviço militar! Faltam {} ano(s)! Seu alistamento será do ano {}!'.format(18 - idade, ano + 18))
elif idade == 18:
    print('Já´é hora de se alistar ao serviço militar!')
else:
    print('Ja passou {} ano(s) do seu tempo de listamento militar! Seu alistamento foi em {}!'.format(idade - 18, ano + 18))
