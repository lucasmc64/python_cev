print('{} DESAFIO 44 {}'.format('='*10, '='*10))
print('\033[31mOBSERVAÇÃO: Use o ponto (.) em vez da vírgula!\033[m')
preco = float(input('Digite o preço do produto: R$'))
metodo = int(input("""POR FAVOR, DIGITE O NÚMERO REFERENTE À FORMA DE PAGAMENTO
(1) À vista (dinheiro/cheque)
(2) À vista (cartão)
(3) Em até 2x (no cartão)
(4) Parcelar 3x ou mais (cartão)\nSua opção: """))
if metodo == 1:
    preco = preco - (preco * 10 / 100)
    print('Você ganhou 10% de desconto! O novo valor a ser pago é de R${}!'.format(preco))
elif metodo == 2:
    preco = preco - (preco * 5 / 100)
    print('Você ganhou 5% de desconto! O novo valor a ser pago é de R${}!'.format(preco))
elif metodo == 3:
    parcel = preco / 2
    print('Não há desconto... O total a ser pago é de {} em 2 parcelas de R${}!'.format(preco, parcel))
elif metodo == 4:
    preco = preco + (preco * 20 / 100)
    parcel = int(input('Em quantas parcelas? '))
    print('Com 20% de juros, o novo preço a ser pago é de R${} em parcelas de R${:.2f} em {}x no cartão!'.format(preco, preco / parcel, parcel))
print('\033[36mParabéns pela compra!!!\033[m' if metodo == 1 or metodo == 2 or metodo == 3 or metodo == 4 else 'Esse comando não existe... Por favor reinicie a compra!')