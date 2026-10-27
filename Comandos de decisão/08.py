i = 1
while i == 1:
  numero_1 = float(input())
  numero_2 = float(input())
  operacao = int(input())
  if operacao == 1:
    media = (numero_1 + numero_2) / 2
    print(f'{media:2f}')
    i = 0
  elif operacao == 2:
    if numero_1 > numero_2:
      dif = numero_1 - numero_2
    else:
      dif = numero_2 - numero_1
    print(f'{dif:.2f}')
    i = 0
  elif operacao == 3:
    prod = numero_1 * numero_2
    print(f'{prod:.2f}')
    i = 0
  elif operacao == 4:
    if numero_2 != 0:
      div = numero_1 / numero_2
      print(f'{div:.2f}')
      i = 0
    else:
      print('Erro')
      i = 0
  else:
    print("Erro")
    i = 0
    