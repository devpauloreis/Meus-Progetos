print('-=-' * 20)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-' * 20)
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
tempo = float(input('Quantos anos de financiamento? '))

meses = tempo * 12
parcela = casa / meses
if parcela <= (salario * 0.3):
    print(f'Para pagar uma casa de {casa} em {tempo} anos a prestação será de R${parcela:.2f}')
    print('Parabéns! Sua solicitação de empréstimo foi aprovada.')
else:
    print(f'Para pagar uma casa de {casa} em {tempo} anos a prestação será de R${parcela:.2f}')
    print('Infelizmente você não atende aos requisitos mínimos para esse empréstimo.')