from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores: ', end= '')
for c in n:
    print(f'{c} ', end= '')
print(f'\nO maior valor sorteado foi {max(n)} \n'
      f'O menor valor soteado foi {min(n)}')

'''
SOLUÇÃO NO YOUTUBE
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
'''

'''
MINHA SOLUÇÃO
from random import randint
maior = 0
menor = 101
tupla0 = 0
tupla = 0
print('Os valores sorteados foram: ', end= '')
for c in range(0, 5):
    tupla = randint(1, 100)
    if tupla > maior:
        maior = tupla
    if tupla < menor:
        menor = tupla
    print(f'{tupla}', end= ' ')
print(f'\nO maior número foi {maior} e o menor número foi {menor}')
'''




#tupla = ((randint(1, 100)),(randint(1, 100)),(randint(1, 100)),(randint(1, 100)),(randint(1, 100)))
#print(f'Os valores sorteados foram: {tupla}')
