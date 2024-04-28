dist = float(input('Qual a distância da sua viagem? '))
if dist <= 200:
    print(f'O valor da sua passagem é: R${(dist * 0.5):.2f}')
else:
    print(f'O valor da sua passagem é: R${(dist * 0.45):.2f}')
