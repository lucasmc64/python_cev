from time import sleep
print('{} DESAFIO 42 {}'.format('='*10, '='*10))
r1 = float(input('Digite o valor da 1ª reta: '))
r2 = float(input('Digite o valor da 2ª reta: '))
r3 = float(input('Digite o valor da 3ª reta: '))
resp = abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r2 - r1) < r3 < r2 + r1
if resp == True:
    print('Essas retas PODEM formar um triângulo!\nPROCESSANDO...')
    sleep(2)
    if r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('É UM TRIÂNGULO \033[31mISÓCELES\033[m!')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É UM TRIÂNGULO \033[34mESCALENO\033[m!')
    elif r1 == r2 == r3:
        print('É UM TRIÂNGULO \033[35mEQUILÁTERO\033[m!')
else:
    print('Sorry, NÃO deu pra formar um triângulo!')
