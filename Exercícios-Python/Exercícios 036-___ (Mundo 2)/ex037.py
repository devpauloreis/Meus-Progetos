n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: \n'
    '[ 1 ] converter para BINÁRIO \n'
    '[ 2 ] converter para OCTAL \n'
    '[ 3 ] converter para HEXADECIMAL')
opc = int(input('Sua opção: '))
if opc == 1:
    nf = bin(n)
    print(f'{n} convertido para BINÁRIO é igual a {nf[2:]}')
elif opc == 2:
    nf = oct(n)
    print(f'{n} convertido para OCTAL é igual a {nf[2:]}')
elif opc == 3:
    nf = hex(n)
    print(f'{n} convertido para HEXADECIMAL é igual a {nf[2:]}')
else:
    print('Opção inválida. Tente novamente!')
    