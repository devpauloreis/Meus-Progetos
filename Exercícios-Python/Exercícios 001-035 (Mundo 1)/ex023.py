print('Analisando números...')
num = int(input('Digite um número: '))
u = num // 1 % 10
print(f'Unidade: {u}')
d = num // 10 % 10
print(f'Dezena:  {d}')
c = num // 100 % 10
print(f'Centena: {c}')
m = num // 1000 % 10
print(f'Milhar:  {m}')
