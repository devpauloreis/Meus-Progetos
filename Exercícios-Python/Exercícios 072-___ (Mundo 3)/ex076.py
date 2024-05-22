lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 2.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
print('-' * 41)
print(f'{' LISTAGEM DE PREÇOS ':^30}')
print('-' * 41)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end= '')
    else:
        print(f'R${lista[pos]:>9.2f}')
print('-' * 41)