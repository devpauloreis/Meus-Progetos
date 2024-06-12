'''
dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[1])'''


'''
teste = list()
teste.append('Paulo')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0], end= ' ')
    print(p[1])
    '''



galera = list()
dado = list()
totmai = totmen = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Foram {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade.')
