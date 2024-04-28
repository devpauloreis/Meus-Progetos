from random import randint
from time import sleep
num = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
nume = int(input('Qual o seu palpite? '))
print('PROCESSANDO...')
sleep(3)
if nume == num:
    print('Parabéns, você VENCEU!!')
else: 
    print(f'Você PERDEU, boa sorte na proxima! O número era: {num}')
