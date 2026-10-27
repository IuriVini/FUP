numero_1 = int(input())
numero_2 = int(input())
soma = 0
multiplicacao = 1
if numero_2 > numero_1:
  for i in range(numero_1, numero_2 +1):
    if i % 2 == 0:
      soma += i
    else:
      multiplicacao = multiplicacao * i
  print(soma)
  print(multiplicacao)
else:
  for i in range(numero_2, numero_1 +1):
    if i % 2 == 0:
      soma += i
    else:
      multiplicacao = multiplicacao * i
  print(soma)
  print(multiplicacao)