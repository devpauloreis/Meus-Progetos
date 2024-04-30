r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
c = 0
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As retas acima PODEM formar um triângulo! ', end= ' ')
    c = 1
else:
    print('As retas acima NÃO PODEM formar um triângulo! ')
if c==1:
    print('Elas formam um triângulo: ')
if r1==r2==r3:
    print('EQUILÁTERO')
elif r1!=r2!=r3:
    print('ESCALENO')
else:
    print('ISÓSCELES')
