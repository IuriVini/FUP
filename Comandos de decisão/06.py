continua = 1
while continua == 1:
  nota_1 = float(input())
  if nota_1 < 0:
    print('Nota invalida')
    continua = 0
  elif nota_1 > 10:
    print('Nota invalida')
    continua = 0
  if continua == 1:
    nota_2 = float(input())
    if nota_2 < 0:
      print('Nota invalida')
      continua = 0
    elif nota_2 > 10:
      print('Nota invalida')
      continua = 0
  if continua == 1:
    nota_3 = float(input())
    if nota_3 < 0:
      print('Nota invalida')
      continua = 0
    elif nota_3 > 10:
      print('Nota invalida')
      continua = 0
  if continua == 1:
    media = (nota_1+nota_2+nota_3) / 3
    print(f'{media:.2f}')
    break