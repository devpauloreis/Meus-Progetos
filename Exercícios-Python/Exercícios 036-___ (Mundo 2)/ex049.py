n = int(input('Informe um número inteiro: '))
print(f'A sua tabuada é: \n'
      '--------------------- \n')
for c in range(1, 10):
    print(f'{n} X {c} = {c * n}')
print('---------------------')
