n = int(input())
s = 1
for i in range(1, n+1):
  linha = ''
  for c in range(1, i+1):
    linha = linha + str(s) + " "
    s += 1
  print(linha)