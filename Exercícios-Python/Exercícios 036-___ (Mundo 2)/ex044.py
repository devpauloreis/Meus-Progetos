print(f'{" MÉTODO DE PAGAMENTO ":=^40}')
preco = float(input('Informe o preço do produto: '))
din = preco - (preco * 0.1)
cart1x = preco - (preco * 0.05)
cart2x = preco
cart3x = preco + (preco * 0.2)
print('Qual a forma de pagamento? ')
print(  '[1] Dinheiro \n'
        '[2] Cartão à vista \n'
        '[3] Cartâo 2x \n'
        '[4] Cartão 3x ou mais \n')
met = int(input('Informe um número de 0 a 10 para escolher a forma de pagamento: '))

if met == 0:
    print(f'O valor com 10% de desconto fica R${din:.2f}')
elif met == 1:
    print(f'O valor com 5% de desconto fica R${cart1x:.2f}')    
elif met == 2:
    print(f'Nessa forma de pagamento não tem desconto e o valor fica R${cart2x}')
elif met >= 3:
    print(f'Nessa forma de pagamento tem acréscimo de {preco * 0.2} e o valor fica R${cart3x}')
    