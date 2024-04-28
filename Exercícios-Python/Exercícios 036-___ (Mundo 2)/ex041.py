from datetime import date
print('-=-' * 20)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-=-' * 20)
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade<10:
    print(f'Sua idade é {idade} e sua categoria é MIRIM')
elif 9<idade<15:
    print(f'Sua idade é {idade} e sua categoria é INFANTIL')
elif 14<idade<20:
    print(f'Sua idade é {idade} e sua categoria é JUNIOR')
elif idade == 20:
    print(f'Sua idade é {idade} e sua categoria é SÊNIOR')
elif idade>20:
    print(f'Sua idade é {idade} e sua categoria é MASTER')
