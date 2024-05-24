lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um valor: ')))
    sn = str(input('Quer continuar? '))
    if sn in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
lista.sort()
par.sort()
impar.sort()
print(f'A lista principal ficou: {lista}')
print(f'A lista de valores pares: {par}')
print(f'A lista de valores ímpares: {impar}')    
    

