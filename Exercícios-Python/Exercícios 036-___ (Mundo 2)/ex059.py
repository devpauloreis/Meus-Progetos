from time import sleep
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
c = 0
while c == 0:
    sleep(1)
    print('[ 1 ] Somar \n'
          '[ 2 ] Multiplicar \n'
          '[ 3 ] Maior \n'
          '[ 4 ] Novos números \n'
          '[ 5 ] Sair')
    opc = int(input('Qual opção você deseja? '))
    if opc == 1:
        print(f'A soma entre {n1} + {n2} é {n1+n2}')
        print('=-='*10)    
    elif opc == 2:
        print(f'A multiplicação entre {n1} x {n2} é {n1 * n2}')
        print('=-='*10)
    elif opc == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
            print('=-='*10)
        else:
            print(f'O maior número entre {n1} e {n2} é {n2}')
            print('=-='*10)
    elif opc == 4:
        n1 = int(input('Informe o novo valor do primeiro número: '))
        n2 = int(input('Informe o novo valor do segundo número: '))
        print('=-='*10)
    elif opc == 5:
        c = 1
        print('Finalizando...')
        print('=-='*10)
        sleep(2)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção inválida. Tente novamente ')
        print('=-='*10)