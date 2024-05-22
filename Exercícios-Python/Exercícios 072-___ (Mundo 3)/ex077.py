lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in lista:
    print(f'Na palavra {c} temos ', end= '')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end= ' ')
    print('')    