a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < b + a:
  if a == b and a == c:
    tipo_do_trinagulo = "equilatero"
  elif a == b and a != c or a != b and a == c or b == c and a != b :
    tipo_do_trinagulo = "isosceles"
  else:
    tipo_do_trinagulo = "escaleno"
  print('Triangulo {}'.format(tipo_do_trinagulo))

else:
  print('Nao triangulo')