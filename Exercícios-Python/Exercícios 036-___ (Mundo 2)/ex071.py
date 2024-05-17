print('===============================')
print('           BANCO CEV          ')
print('===============================')
valor = int(input('Que valor você quer sacar? R$'))
c50 = valor // 50
sobra = valor - c50*50
c20 = sobra // 20
sobra = sobra - c20*20
c10 = sobra // 10
sobra = sobra - c10*10
c1 = sobra
print(f'Total de {c50} cédulas de R$50 \n'
      f'Total de {c20} cédulas de R$20 \n'
      f'Total de {c10} cédulas de R$10 \n'
      f'Total de {c1} cédulas de R$1 \n'
      '=============================== \n'
      'Volte sempre ao BANCO CEV! Tenha um bom dia!')
