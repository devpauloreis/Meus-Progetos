while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(0, 10):   
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERADO')    
        