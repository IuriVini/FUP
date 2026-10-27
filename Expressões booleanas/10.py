def funcao(x1, x2):
  divisao = x1 % x2
  while divisao != 0:
    x1 = x2 
    x2 = divisao 
    divisao = x1 % x2
  return x2