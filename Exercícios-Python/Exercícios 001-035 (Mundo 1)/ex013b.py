valor = float(input('Qual o valor bruto do produto? '))
print(f'O produto de valor R${valor} na forma de pagamento: \n'
      f'A vista R${(valor - valor * 0.1):.2f} \n'
      f'A prazo R${(valor + valor * 0.08):.2f}')
