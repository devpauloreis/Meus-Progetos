n = int(input('Informe um número: '))
d = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[34m', end= '')
        d += 1
    else:
        print('\033[m', end= '')
    print(f'{c}', end= ' ')
print('')    
if d == 2:
    print(f'\033[mO número {n} foi divisível {d} vezes.\n'
          'E por isso, ele É PRIMO')
else:
    print(f'\033[mO número {n} foi divisível {d} vezes.\n' 
          'E por isso, ele NÃO É PRIMO')



"""if d == 1:
    print('Esse número é PRIMO')        
else:
    print('Esse número NÃO é primo')
"""