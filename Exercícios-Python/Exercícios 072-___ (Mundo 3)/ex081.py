lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    sn = str(input('Quer continuar? '))
    if sn in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores ')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {lista}')
c2 = 0
if 5 in lista:
    for c, c1 in enumerate(lista):
        if c1 == 5:
            c2 = c
    print(f'O valor 5 foi digitado e está na posição {c2+1}')
else:
    print('O valor 5 não faz parte da lista')