print('{} DESAFIO 38 {}'.format('='*10, '='*10))
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O \033[34mPRIMEIRO\033[m valor é maior!')
elif n2 > n1:
    print('O \033[32mSEGUNDO\033[m valor é maior!')
else:
    print('Não existe valor maaior, os dois são \033[36mIGUAIS\033[m!')
#Se forem digitadas letras em vez de números dá erro!
