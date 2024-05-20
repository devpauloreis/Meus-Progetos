from datetime import date
ano = int(input('Em que ano você nasceu? '))
year = date.today().year
idade = year - ano
atraso = idade - 18 
if idade > 18:
    print('Já passou do tempo para se alistar... \n'
          f'Você está atrasado em {atraso} anos.')
elif idade == 18:
    print('Você está na hora de se alistar, cuidado para não perder o prazo! ')
else: 
    atraso = 18 - idade
    print(f'Você ainda é novo, seu alistamento é daqui a {atraso} anos.')
