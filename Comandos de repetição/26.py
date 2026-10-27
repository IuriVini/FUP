import math
def funcao(x,n):
  soma = 0.0
  for i in range(x +1):
    expoente = i * 2 + 1
    sinal = (-1) ** i
    termo = sinal * (x ** expoente) / math.factorial(expoente)
    soma += termo
  return soma  