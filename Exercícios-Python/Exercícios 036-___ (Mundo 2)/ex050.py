par = 0
s = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        par += 1
print(f'Você informou {par} números PARES e a soma deles é {s}')