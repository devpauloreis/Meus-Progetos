maior = 0 
menor = 99999999
for c in range(0, 5):
    peso = float(input(f'Qual o peso da pessoa {c+1}? '))
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso

print(f'O maior peso lido foi {maior} e o menor foi {menor}.')
