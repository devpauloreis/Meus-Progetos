print('---------------------------')
print('Sequência de Fibonacci')
print('---------------------------')
n = int(input('Quantos termos você quer que eu mostre? '))
n1 = 0
n2 = 1
n3 = 0
c = 0
print(f'{n1} -> ', end= '')
print(f'{n2} -> ', end= '')
while c < (n-2):
    n3 = n1 + n2
    print(f"{n3} -> ", end= '')
    n1 = n2
    n2 = n3 
    c += 1
print('FIM')