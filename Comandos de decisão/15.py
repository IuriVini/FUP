n = int(input())
soma = 0
for divisor in range(1, n):
  if n % divisor == 0:
    soma += divisor
  else:
    soma += 0
print(soma)