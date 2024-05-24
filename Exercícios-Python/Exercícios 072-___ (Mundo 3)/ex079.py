lista = list()
cont = 1
sn = ''
while True:
    n = int(input(f'Digite o {cont}º número: '))
    if n not in lista:
        print('Adicionado com sucesso! ')
        lista.append(n)
        cont += 1
    else:
        print('Este número ja esta na lista, não vou adicionar... ')
    while 'SN' not in sn:
        sn = input('Quer continuar? [S/N] ').upper()
        if sn in 'SN':
            break
    if sn == 'N':
        break
lista.sort()
print('-=' * 30)
print(f'Você adicionou os valores {lista}')