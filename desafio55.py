print('{} DESAFIO 55 {}'.format('='*10, '='*10))
mai = 0
men = 0
for i in range(0, 5):
    p = int(input('Digite seu peso: '))
    if(i == 0):
        mai = p
        men = p
    elif(p < men):
        men = p
    elif(p > mai):
        mai = p
print('{}kg é o maior peso'.format(mai))
print('{}kg é o menor peso'.format(men))