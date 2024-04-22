from math import sqrt
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
h = sqrt(co**2 + ca**2)

print(f'Dado o cateto oposto {co} e o cateto adjacente {ca}, o valor da hipotenusa será: {h}')
