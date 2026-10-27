n = str(input())
tamanho = len(n)
novo = ''
for i in range(0, tamanho):
  numero = n[i]
  if numero == '0':
    novo = novo + '1'
  elif numero == '1':
    novo = novo + '1'
  else:
    novo = novo + numero
print(novo)