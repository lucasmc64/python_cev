print('{} DESAFIO 8 {}'.format('='*10, '='*10))
m = float(input('Digite o valor em metros: '))
km = m / 1000
ht = m / 100
dm = m / 10
dcm = m * 10
cm = m * 100
mm = m * 1000
print('Você digitou \033[31m{}m\033[m. Isso equivale a:\033[34m\n{}km \n{}ht \n{}dm \n{}dcm \n{}cm \n{}mm\033[m!'.format(m, km, ht, dm, dcm, cm, mm))
