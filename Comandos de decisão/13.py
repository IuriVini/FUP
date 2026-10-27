def funcao(a , b , c):
  if a !=0: 
    delta = b**2 - 4*a*c
    if delta < 0:
      return 0.0, 0.0, '1'
    elif delta == 0:
      x1 = (-b) / (2 * a)
      return x1, x1, '2'
    else:
      x1 = (-b + delta ** 0.5) / (2 * a) 
      x2 = (-b - delta ** 0.5) / (2 * a) 
      return x1, x2, '3'
  else:
    return 0.0,0.0,'0'

a = float(input())
b = float(input())
c = float(input())
x1, x2, c = funcao(a, b, c)

if c == '0':
  print('Nao eh equacao do 2o grau')
elif c == '1':
  print('Nao existe raiz real')
elif c == '2':
  print(f'{x1:.2f}')
  print('Raiz unica')
else:
  print(f'{x1:.2f}')
  print(f'{x2:.2f}')
