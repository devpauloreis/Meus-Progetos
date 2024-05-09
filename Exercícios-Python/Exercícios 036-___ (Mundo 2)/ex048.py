val = 0
s = 0
for c in range(0,501):
    if c%3==0 and c%2==1:
        s += c
        val += 1
print(f'A soma entre os {val} números solicitados é: {s}')
