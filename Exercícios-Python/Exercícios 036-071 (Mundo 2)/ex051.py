print('========================= \n'
      ' PROGRESSÃO ARITIMÉTICA \n'
      '=========================')
termo1 = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão: '))
n = termo1
for c in range(0, 10):
    print(f'{n} ---', end= ' ')
    n += r
print('ACABOU')