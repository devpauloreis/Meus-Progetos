
tot18 = 0
totH = 0
totM20 = 0
while True:
    sexo = ''
    SN = ''
    print('---------------------------')
    print('   CADASTRE UMA PESSOA     ')
    print('---------------------------')
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]
    print('---------------------------')
    while SN != 'S' and SN != 'N':
        SN = input('Quer continuar? [S/N] ').strip().upper()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    if SN == 'N':
        break
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {tot18} \n'
      f'Ao todo temos {totH} homens cadastrados \n'
      f'E temos {totM20} mulheres com menos de 20 anos ')
