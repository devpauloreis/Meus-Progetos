expr = str(input('Digite uma expressão: '))
pilha = []
for simb in pilha:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0 :
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')