from random import randint
print('-=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*15)
c = 0
b = 0
while True:
    escolhajg = int(input('Diga um valor: '))
    player = input('Par ou ímpar? [P/I] ').strip().upper()
    escolhapc = randint(0,10)
    soma = escolhajg + escolhapc
    print('----------------------------------')
    if soma % 2 == 0:
        print(f'Você jogou {escolhajg} e o computador jogou {escolhapc}. Total DEU PAR ')
        print('----------------------------------')
    elif soma % 2 == 1:
        print(f'Você jogou {escolhajg} e o computador jogou {escolhapc}. Total DEU ÍMPAR ')
        print('----------------------------------')
    if player == 'P' and soma % 2 == 0:
        print('Você GANHOU!')
        c += 1
    elif player == 'I' and soma % 2 == 1:
        print('Você GANHOU!')
        c += 1
    elif player == 'P' and soma % 2 == 1:
        print('Você PERDEU!')
        break
    elif player == 'I' and soma % 2 == 0:
        print('Você PERDEU!')
        break
print('=-' * 20)
if c == 1:
    print(f'GAME OVER! Você venceu {c} vez.')
else:    
    print(f'GAME OVER! Você venceu {c} vezes.')
