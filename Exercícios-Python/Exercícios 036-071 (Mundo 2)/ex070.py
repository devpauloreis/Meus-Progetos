print('------------------------------------------------')
print('             LOJA SUPER BARATÃO                 ')
print('------------------------------------------------')
N = ''
preco = 0
SN = ''
total = 0
mais1k = 0
menorpreco = 99999999
barato = ''
while True:
    N = input('Nome do produto: ')
    preco = float(input('Preço: '))
    total += preco
    while SN not in ['S','N']:
        SN = input('Quer continuar? [S/N] ').strip().upper()[0]
    if preco > 1000:
        mais1k += 1
    if preco < menorpreco:
        menorpreco = preco
        barato = N
    if SN == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${total:.2f} \n'
      f'Temos {mais1k} produtos custando mais de R$1000.00 \n'
      f'O produto mais barato foi {barato} que custa R${menorpreco:.2f}')
