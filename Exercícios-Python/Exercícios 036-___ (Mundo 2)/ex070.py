print('------------------------------------------------')
print('             LOJA SUPER BARATÃO                 ')
print('------------------------------------------------')
N = ''
preco = 0
SN = ''
total = 0
mais1k = 0
menorpreco = 99999999
nomebarato = ''
while True:
    N = input('Nome do produto: ')
    preco = float(input('Preço: '))
    SN = input('Quer continuar? [S/N] ').strip().upper()
    total += preco
    if preco > 1000:
        mais1k += 1
    if preco < menorpreco:
        menorpreco = preco
        nomebarato = N
    if SN == 'N':
        break
print('---------------- FIM DO PROGRAMA ---------------')
print(f'O total da compra foi R${total:.2f} \n'
      f'Temos {mais1k} produtos custando mais de R$1000.00 \n'
      f'O produto mais barato foi {nomebarato} que custa R${menorpreco:.2f}')
