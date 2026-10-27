def funcao(x):
  f1 = 0
  f2 = 1
  for f in range (1, x+1):
      proximo = f1 + f2
      f1 = f2
      f2 = proximo
  return f1