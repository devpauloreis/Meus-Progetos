nome = ' '
idade = 0
sexo = ' '
maior = 0
maisvelho = ' '
menos = 0
idades = 0
for c in range(0, 4):
    nome = input(f'Qual o nome da pessoa {c+1}? ')
    idade = int(input(f'Qual a idade da pessoa {c+1}? '))
    sexo = input(f'Qual o sexo da pessoa {c+1}? [M/F] ')
    idades += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            maisvelho = nome
    else:
        if idade < 21:
            menos += 1
m = idades // 4
print(f'A média de idade do grupo é {m}. \n'
      f'O nome do homem mais velho é {maisvelho}. \n'
      f'A quantidade de mulheres com menos de 21 anos é {menos}')
