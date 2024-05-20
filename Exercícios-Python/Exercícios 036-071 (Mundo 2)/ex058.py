from random import randint
print('JOGO DE ADIVINHAÇÃO')
print('Vou pensar em um número e você vai tentar adivinhar. ')
palpite = 0
tentativas = 0
pc = randint(0, 10)
while palpite != pc:
    palpite = int(input('Qual o seu palpite? '))
    tentativas += 1
    if palpite == pc:
        print(f'Parabéns depois de {tentativas} tentativas você acertou. ')
    elif palpite > pc:
        print('Menos... Tente mais uma vez. ')
    else:
        print('Mais... Tente mais uma vez. ')
