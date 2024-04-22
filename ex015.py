dias = float(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual a quantidade de Km rodados? '))
print(f'O total a pagar é de R${((dias * 60) + (km * 0.15)):.2f}')