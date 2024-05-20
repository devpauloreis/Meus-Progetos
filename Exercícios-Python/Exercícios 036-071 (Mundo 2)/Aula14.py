'''n = int(input('Digite até qual número eu devo contar: '))
c = 0
while c != n+1:
    print(c)
    c += 1
print('FIM')'''

s = str(input('Digite seu sexo: [M/F] '))
while s not in 'MmFf':
    s = str(input('Dados inválidos. Por favor informe seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')
