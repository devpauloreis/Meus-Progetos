print('Analisando seu nome...')
nome = input('Digite seu nome completo: ')
nome = nome.strip()
print('Seu nome em letras maiúsculas: ', end= ' ')
print(nome.upper())
print('Seu nome em letras minúsculas: ', end= ' ')
print(nome.lower())
print('Quantas letras ao todo(sem considerar espaços): ', end= ' ')
caracteres = len(nome)
nomecount = nome.count(' ')
caracteres = caracteres - nomecount
print(caracteres)
print('Quantas letras tem o primeiro nome: ', end= ' ')
separa = nome.split()
letrassepara = len(separa[0])
print(f'Seu primeiro nome é {separa[0]} e tem {letrassepara} letras')
