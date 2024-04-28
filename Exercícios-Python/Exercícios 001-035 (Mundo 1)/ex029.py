kmh = float(input('Qual a velocidade atual do carro? '))
if kmh > 80:
    print(f'Você está acima da velocidade permitida, sua multa é de R${((kmh - 80) * 7.0):.2f}') 
else: 
    print('Você está dentro do limite de velocidade, continue assim!!!')    
