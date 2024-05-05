from time import sleep
from random import choice
itens = ('Pedra', 'Papel', 'Tesoura')
print('Suas opções: ')
print('[1] PEDRA \n'
      '[2] PAPEL \n'
      '[3] TESOURA')
escolhajgn = int(input('Qual a sua jogada? '))
jogador = itens[escolhajgn - 1]
pc = choice(itens)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if jogador == pc:
    print('Deu EMPATE')
elif jogador == 'Pedra' and pc == 'Papel':
    print('EU GANHEIIII HAHAHA')
elif jogador == 'Pedra' and pc == 'Tesoura':
    print('Que ódio, você me venceu...')
elif jogador == 'Papel' and pc == 'Pedra':
    print('Que ódio, você me venceu...')
elif jogador == 'Papel' and pc == 'Tesoura':
    print('EU GANHEIIII HAHAHA')
elif jogador == 'Tesoura' and pc == 'Pedra':
    print('EU GANHEIIII HAHAHA')
elif jogador == 'Tesoura' and pc == 'Papel':
    print('Que ódio, você me venceu...')
print(f'Você escolheu {jogador} e eu escolhi {pc}.')