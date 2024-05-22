umavinte = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze', 'Dezesseis', 'Dezessete','Dezoito',
            'Dezenove','Vinte')
n = 0
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <=20:
            break
        print('Tente novamente.', end= ' ')
    print(f'Você digitou o número {umavinte[n]}')
    sn = input('Quer continuar? [S/N] ').strip().upper()
    if sn == 'N':
        break
print('Fim do programa!')