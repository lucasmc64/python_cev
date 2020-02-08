print('{} DESAFIO 43 {}'.format('='*10, '='*10))
print('\033[31mOBSERVAÇÃO: Use o ponto (.) em vez da vírgula!\033[m')
peso = float(input('Digite o peso em kilogramas: '))
alt = float(input('Digite sua altura em metros '))
imc = peso / alt ** 2
print('Seu IMC é {:.2f}!'.format(imc))
if imc <= 18.5:
    print('ABAIXO DO PESO!')
elif 18.5 < imc <= 25:
    print('ESTÁ NO PESO IDEAL!')
elif 25 < imc <= 30:
    print('ACIMA DO PESO!')
elif 30 < imc <= 40:
    print('OBESIDADE!')
elif 40 < imc:
    print('OBESIDADE MÓRBIDA!')
