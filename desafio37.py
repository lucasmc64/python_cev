print('{} DESAFIO 37 {}'.format('='*10, '='*10))
n = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para a conversão:
(1) BINÁRIO
(2) OCTAL
(3) HEXADECIMAL""")
op = int(input('Sua opção: '))
if op == 1:
    print('\033[32m{}\033[m convertido para BINÁRIO é igual a \033[32m{}\033[m!'.format(n, bin(n)[2:]))
elif op == 2:
    print('\033[33m{}\033[m convertido para OCTAL é igual a \033[33m{}\033[m!'.format(n, oct(n)[2:]))
elif op == 3:
    print('\033[34m{}\033[m convertido para HEXADECIMAL é igual a \033[34m{}\033[m!'.format(n, hex(n)[2:].upper()))
else:
    print('\033[31mOPÇÃO INVÁLIDA! Por favor, tente novamente!\033[m')