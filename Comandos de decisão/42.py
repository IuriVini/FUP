frase = str(input())
tamanho = len(frase)
espacos = 0
for i in range(0, tamanho):
  letra = frase[i]
  if letra == ' ':
    espacos += 1
print(espacos)