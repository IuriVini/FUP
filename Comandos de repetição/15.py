def funcao(x):
  e = 1.0
  fatorial = 1
  for i in range(1, x+1):
    fatorial *= i
    e = e + (1/fatorial)
  return e