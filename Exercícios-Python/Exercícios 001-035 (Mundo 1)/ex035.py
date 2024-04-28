print('-=-' * 20)
print('Analisador de Triângulos')
r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('As retas acima PODEM formar um triângulo! ')
else:
    print('As retas acima NÃO PODEM formar um triângulo! ')
