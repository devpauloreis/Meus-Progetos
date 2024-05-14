sn = 0
n = 1
c = 'S'
c1 = 0
c2 = 5
maior = 0
menor = 99999
cont = 0
while c == 'S': 
    n = int(input('Digite um número: '))
    sn += n
    c1 += 1
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    if maior < n:
        maior = n
    if menor > n:
        menor = n
m = sn / cont
print(f'Foram digitados {c1} números \n' 
      f'A soma de todos eles é {sn} \n'
      f'A média entre eles é {m:.2f} \n'
      f'O maior é {maior} \n'
      f'O menor é {menor}')