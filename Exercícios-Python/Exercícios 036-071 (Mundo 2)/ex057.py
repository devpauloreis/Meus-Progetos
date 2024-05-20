s = str(input('Digite seu sexo: [M/F] ')).strip().upper()
while s not in ['M', 'F']:
    s = str(input('Dados inválidos. Por favor informe seu sexo: [M/F] ')).strip().upper()
print(f'Sexo {s} registrado com sucesso!')
