import math
maior = -math.inf
quant_maior = 0
vezes = int(input())
for i in range(1, vezes+1):
  numero = int(input())
  if numero > maior:
    maior = numero
    quant_maior = 1
  elif numero == maior:
    quant_maior +=1
print(maior)
print(quant_maior)