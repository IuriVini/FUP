numero = int(input())
if numero >= 0:  
  maior = numero
  menor = numero
  while numero >= 0:
    numero = int(input())
    if numero > maior:
      maior = numero
    elif numero < maior:
      if numero < 0:
        menor = menor
      elif menor > numero:
        menor = numero
      elif menor < numero:
        menor = menor
    elif numero == maior:
      maior = maior
  print(maior)
  print(menor)
else:
  print()