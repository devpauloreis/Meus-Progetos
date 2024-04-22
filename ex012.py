preco = float(input('Qual o valor do produto sem o desconto? '))
desc = (preco * (5/100))
print(f'O valor do produto com o desconto de 5% é {(preco - desc):.2f}')
