'''n = list()
cont = 1  
cont1 = 0
num = 0
sn = ''
while True:
    num = int(input(f'Digite o {cont}º valor: '))
    for c in n:
        if c == (num):
            n.insert(num, cont1)
        cont1 += 1
    cont1 = 0
    cont += 1
    while 'SN' not in sn:
        sn = input('Quer continuar? [S/N] ').upper()
        if sn in 'SN':
            break
    if sn == 'N':
        break
print('-=' * 30)
print(f'Você adicionou os valores {n}')'''


'''lista = list()
num = 0
cont = 0
lista.append(int(input('Digite um número: ')))
for c in range(0, 4):
    num = int(input('Digite um número:'))
    for c1 in lista:
        if c1 == num:
            lista.insert(cont, num)

print(lista)
    '''

lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram: {lista}')

























