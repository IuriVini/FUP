def funcao(x):
  fator_primo = 0
  for divisor in range(2, x+1):
    if x % divisor == 0:
      primo = 0
      for c in range(1, divisor +1):
        if divisor % c == 0:
              primo += 1
      if primo <= 2:
        fator_primo = divisor
  return fator_primo