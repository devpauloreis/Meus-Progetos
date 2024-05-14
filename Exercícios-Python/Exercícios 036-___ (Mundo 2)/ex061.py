print('Gerador de PA')
print('-=-' * 10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
while c != 10:
    print(f'{termo1} -> ', end= '')
    termo1 += razao
    c += 1
print('FIM')    