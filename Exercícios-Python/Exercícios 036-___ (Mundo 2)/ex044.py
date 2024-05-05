print('MÉTODO DE PAGAMENTO')
preco = float(input('Informe o preço do produto: '))
din = preco - (preco * 0.1)
cart1x = preco - (preco * 0.05)
cart2x = preco
cart3x = preco + (preco * 0.2)
print('Qual a forma de pagamento? ')
print(  '[0] Dinheiro \n'
        '[1] Cartão à vista \n'
        '[2] Cartâo 2x \n'
        '[3] Cartão 3x \n'               
        '[4] Cartão 4x \n'                
        '[5] Cartão 5x \n'             
        '[6] Cartão 6x \n'                
        '[7] Cartão 7x \n'                
        '[8] Cartão 8x \n'                
        '[9] Cartão 9x \n'                
        '[10] Cartão 10x \n')
met = int(input('Informe um número de 0 a 10 para escolher a forma de pagamento: '))

if met == 0:
    print(f'O valor com 10% de desconto fica R${din:.2f}')
elif met == 1:
    print(f'O valor com 5% de desconto fica R${cart1x:.2f}')    
elif met == 2:
    print(f'Nessa forma de pagamento não tem desconto e o valor fica R${cart2x}')
elif met >= 3:
    print(f'Nessa forma de pagamento tem acréscimo de 20% e o valor fica R${cart3x}')
    