nome = str(input('Digite seu nome completo: '))
nome = nome.title().split()
print(f'Muito prazer, {nome[0]} \n'
      f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome[-1]}')

'''
ooouu
nome = str(input('Digite seu nome completo: '))
nome = nome.title().split()
print(f'Muito prazer, {nome[0]} \n'
      f'Primeiro nome: {nome[0]}')
print(f'Último nome: {nome.pop()}')
                      ^^^^^^^^^^^
'''