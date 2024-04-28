print('-=-' * 20)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-' * 20)
casa = float(input('Qual o valor da casa que você quer comprar? R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = float(input('Em quantos anos você pretende pagar? '))

tempo = tempo * 12
parcela = casa / tempo
if parcela <= (salario * 0.3):
    print('Parabéns! Sua solicitação de empréstimo foi aprovada.')
else:
    print('Infelizmente você não atende aos requisitos mínimos para esse empréstimo.')