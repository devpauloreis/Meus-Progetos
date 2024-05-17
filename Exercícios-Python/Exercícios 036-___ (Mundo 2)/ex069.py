
maior18 = 0
masc = 0
fem = 0
sexo = ''
SN = ''
while True:
    sexo = ''
    SN = ''
    print('---------------------------')
    print('   CADASTRE UMA PESSOA     ')
    print('---------------------------')
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').strip().upper()
    print('---------------------------')
    while SN != 'S' and SN != 'N':
        SN = input('Quer continuar? [S/N] ').strip().upper()
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        fem += 1
    if SN == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {maior18} \n'
      f'Ao todo temos {masc} homens cadastrados \n'
      f'E temos {fem} mulheres com menos de 20 anos ')
