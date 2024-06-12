'''nomepeso = list()
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
print(f'O menor peso foi de {menorp:.2f}Kg. Peso de {menor[0]}')'''

'''
nomepeso = []
dados = []
maiorpt = ['', 0]
maiorp = []
menorp = []
sn = ''
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    nomepeso.append(dados[:])
    dados.clear()
    sn = str(input('Quer continuar? [S/N] ')).strip().upper()
    if sn == 'N':
        break
for p in nomepeso:
    if p[1] >= maiorpt[1]:
        maiorp.append(p[:])
print(f'Foram {len(nomepeso)} pessoas cadastradas.')
print(f'E o maior peso foi {maiorp}')
print(nomepeso)
'''



dados = []
pessoas = []
SN = ''
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    SN = input('Quer continuar? [S/N] ')
    if SN in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maiorp}Kg. O peso de ', end= '')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end= ' ')
print('')
print(f'O menor peso foi {menorp}Kg. O peso de ', end= '')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}]', end= ' ')

'''
Esse aqui foi uma luta pra sair, rapaz...
'''