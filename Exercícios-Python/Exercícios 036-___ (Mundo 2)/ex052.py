n = int(input('Informe um número: '))
d = 0
for c in range(1, n):
    if n % c == 0:
        d += 1 
if d == 1:
    print('Esse número é PRIMO')        
else:
    print('Esse número NÃO é primo')    