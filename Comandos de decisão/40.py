n = str(input())
vezes = 0
tamanho = len(n)
for i in range(0, tamanho):
  letra = n[i]
  if letra == '1':
    vezes += 1
print(vezes)