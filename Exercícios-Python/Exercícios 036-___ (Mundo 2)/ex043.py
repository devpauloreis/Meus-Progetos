print('-=-' * 10)
print('Calculador de IMC')
print('-=-' * 10)
peso = float(input('Informe o seu peso: (Kg) '))
altura = float(input('Informe a sua altura: (m) '))
imc = peso / altura**2
print(f'O seu IMC é {imc:.2f}, e de acordo com a tabela sua categoria é: ', end= '')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO') 
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
