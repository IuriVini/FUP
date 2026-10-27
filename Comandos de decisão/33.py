numero = int(input())
soma = 0
for divisor in range(1, numero):
  if numero % divisor == 0:
    soma += divisor
if soma == numero:
  print('Perfeito')
else:
  print('Nao perfeito')