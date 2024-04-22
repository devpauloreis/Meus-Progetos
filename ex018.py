from math import cos,sin,tan,radians
a = float(input('Informe o valor do ângulo: '))
ar = radians(a)
print(f'O ângulo de {a} tem o SENO de {sin(ar):.2f} \n' 
      f'O ângulo de {a} tem o COSSENO de {cos(ar):.2f} \n'
      f'O ângulo de {a} tem a TANGENTE de {tan(ar):.2f}')
