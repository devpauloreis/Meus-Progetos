import random
print('-=-' * 10)
print('JOKENPÔ')
print('-=-' * 10)
pc = random.randint(1, 3)
print('[1] PEDRA \n'
      '[2] PAPEL \n'
      '[3] TESOURA')
player = int(input('Escolha de 1 a 3 qual a sua jogada: '))
if pc == player:
    print('EMPATE')
elif player == 1 and pc == 2:
    print('EU GANHEI HAHAHA')
elif player == 1 and pc == 3:
    print('VOCÊ GANHOU \n'
          f'Eu escolhi {pc}')

elif player == 2 and pc == 3:
    print('EU GANHEI HAHAHA')
elif player == 2 and pc == 1:
    print('VOCÊ GANHOU \n'
          f'Eu escolhi {pc}')

elif player == 3 and pc == 1:
    print('EU GANHEI HAHAHA')
elif player == 3 and pc == 2:
    print('VOCÊ GANHOU \n'
          f'Eu escolhi {pc}')
