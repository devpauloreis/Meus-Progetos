print('Gerador de PA')
print('-=-' * 10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0 #contador do while
c1 = 10 #quantidade de vezes que o while vai rodar
termosmostrados = c1
while c < c1 and c1 != 0:
    print(f'{termo1} -> ', end= '')
    if c == (c1-1):
        print('PAUSA')
        c1 = int(input('Quer mais quantos termos? '))
        termosmostrados += c1
        c = -1
    termo1 += razao
    c += 1
print(f'A progressão foi finalizada com {termosmostrados} termos mostrados. ')