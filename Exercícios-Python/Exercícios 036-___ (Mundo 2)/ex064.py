sn = 0
n = 0
c = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999: 
    sn += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitados {c} números e a soma de todos eles é {sn}')