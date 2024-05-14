from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
print(f'Calculando {n}! =', end= ' ')
sn = factorial(n)
while n != 0:
    print(f'{n} ',end= '')
    print('x ' if n > 1 else '= ', end= '')
    n -= 1
print(f'{sn}')


''' print(f'{n} ', end= '')
    if n != 1:
        print('x ', end= '')
    if n != 1:
        sn = sn * (n - 1) '''
