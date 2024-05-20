import datetime
maior = 0
menor = 0
for c in range(0,7):
    ano = int(input(f'Qual o ano de nascimento da {c+1}ª pessoa ? '))
    idade = datetime.date.today().year - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Dentre as idades informadas, {maior} são maiores de idade e {menor} são menores. ')     