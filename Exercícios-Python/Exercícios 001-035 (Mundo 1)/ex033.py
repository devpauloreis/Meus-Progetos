a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'O MENOR valor digitado foi: {menor} \n'
      f'O MAIOR valor digitado foi: {maior}')