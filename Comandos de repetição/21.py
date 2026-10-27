def funcao(x):
  for c in range(x):
    espacos = ' ' * (x - 1 - c)
    asterisco = '*' * (2 * c +1)
    print(espacos + asterisco)