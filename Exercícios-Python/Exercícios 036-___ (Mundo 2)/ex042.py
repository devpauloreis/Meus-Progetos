print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As retas acima PODEM formar um triângulo ', end= '')
    if r1==r2==r3:
        print('EQUILÁTERO!')
    elif r1!=r2 and r1!=r3 and r2!=r3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')    
else:
    print('As retas acima NÃO PODEM formar um triângulo! ')
