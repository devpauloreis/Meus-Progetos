n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é: {m}')
if m<5:
    print('Você está REPROVADO!!! ')
elif m>=5 and m<7: 
    print('Você está em RECUPERAÇÃO!!!')
elif m>=7:
    print('Parabéns, você foi APROVADO!!!')
