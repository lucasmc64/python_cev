print('{} DESAFIO 36 {}'.format('='*10, '='*10))
val = float(input('Qual é o valor da casa? '))
sal = float(input('Quanto é o salário do possível comprador? R$'))
anos = int(input('Em quantos anos ele vai pagar? '))
prestacao = val / (anos * 12)
if prestacao > ((sal * 30) / 100):
    print('\033[31mEMPRÉSTIMO NEGADO! O valor da prestação mensal R${:.2f} ultrapassa o limite de 30% do salário.'.format(prestacao))
elif prestacao <= ((sal * 30) / 100):
    print('\033[32mEMPRÉSTIMO APROVADO! Meus parabéns! O valor a ser pago mensalmente é de R${:.2f}!'.format(prestacao))