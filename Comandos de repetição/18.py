n = int(input())
fatorial = 1
soma = 0
for f in range(1,n+1):
  fatorial *= f
for i in range(100):
  soma += fatorial % 10
  fatorial = fatorial // 10
