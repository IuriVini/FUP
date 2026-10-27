s = 0
while s != 5:
  print('1 - Adicao')
  print('2 - Subtracao')
  print('3 - Multiplicacao')
  print('4 - Divisao')
  print('5 - Saida')
  operacao = int(input())
  if operacao == 1:
    valor_1 = float(input())
    valor_2 = float(input())
    adicao = valor_1 + valor_2
    print(f'{adicao:.2f}')
    s = 1
  elif operacao == 2:
    valor_1 = float(input())
    valor_2 = float(input())
    sub = valor_1 - valor_2
    print(f'{sub:.2f}')
    s = 2
  elif operacao == 3:
    valor_1 = float(input())
    valor_2 = float(input())
    Mul = valor_1 * valor_2
    print(f'{Mul:.2f}')
    s = 3  
  elif operacao == 4:
    valor_1 = float(input())
    valor_2 = float(input())
    Divisao = valor_1 / valor_2
    print(f'{Divisao:.2f}')
    s = 4
  else:
    s = 5