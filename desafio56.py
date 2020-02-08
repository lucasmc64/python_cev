print('{} DESAFIO 56 {}'.format('='*10, '='*10))
nome = ''
idade = 0
sexo = ''
media = 0
nmv = ''
imv = 0
cont = 0
for c in range(0, 4):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite o seu sexo: (F/M)').upper()
    if(sexo == 'M'):
        if(c == 0):
            nmv = nome
            imv = idade
        elif(idade > imv ):
            nmv = nome
            imv = idade
    media = media + idade
    if(sexo == 'F'):
        if(idade < 20):
            cont = cont + 1
print('A média das idades é {}'.format(media/4))
print('O homem mais velho é {}'.format(nmv))
print('{} mulheres tem menos de 20 anos'.format(cont))