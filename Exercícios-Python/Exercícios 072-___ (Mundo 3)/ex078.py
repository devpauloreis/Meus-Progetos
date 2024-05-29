lista = []
posmax = [] 
posmin = []
for c in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {c+1}: ')))
for c, p in enumerate(lista):
    if p == max(lista):
        posmax.append(c+1)
    if p == min(lista):
        posmin.append(c+1)
print(f'A lista ficou: {lista}')
print(f'O maior valor informado foi {max(lista)} na posição ', end= '')
for c in posmax:
    print(f'{c}... ', end= '')
print('')
print(f'O menor valor informado foi {min(lista)} na posição ', end= '')
for c in posmin:
    print(f'{c}... ', end= '')
print('')