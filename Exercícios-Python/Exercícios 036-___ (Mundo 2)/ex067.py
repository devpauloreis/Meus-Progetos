n = 2
cont = 1
while True:
    cont = 1
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*15)
    while cont < 11:   
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    print('-'*15)
    if n < 0:
        print('PROGRAMA DE TABUADA ENCERADO')