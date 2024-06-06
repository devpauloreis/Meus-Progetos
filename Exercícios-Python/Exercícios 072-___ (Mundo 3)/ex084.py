nomepeso = list()
cadastro = list()
sn = ''
maiorp = 0
menorp = 999
maior = list()
menor = list()
cad = 0
while True:
    nomepeso.append(str(input('Nome: ')))
    nomepeso.append(int(input('Peso: ')))
    cad += 1
    cadastro.append(nomepeso[:])
    nomepeso.clear
    sn = input('Quer continuar? [S/N] ').strip().upper()
    if sn == 'N':
        print('-=' * 20)
        break
for p in cadastro:
    if p[1] > maiorp:
        maior.append(p[:])
        maiorp = p[1]
    if p[1] < menorp:
        menor.append(p[:])
        menorp = p[1]

print(f'Ao todo, você cadastrou {cad} pessoas.')
print(f'O maior peso foi de {maiorp:.2f}Kg. Peso de {maior[0]}')
print(f'O menor peso foi de {menorp:.2f}Kg. Peso de {menor[0]}')