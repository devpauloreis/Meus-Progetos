sal = float(input('Qual o seu salário? R$'))
if sal > 1250:
    aumento = sal * 0.1
    sal = sal + aumento
else:
    aumento = sal * 0.15
    sal = sal + aumento
print(f'Parabéns, você recebeu um aumento de R${aumento:.2f} e seu novo salário é de R${sal:.2f}')