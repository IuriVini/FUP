primeiro_numero  = float(input())
operacao = str(input())
segundo_numero  = float(input())
if operacao == '+':
  soma = primeiro_numero + segundo_numero
  print(f'{soma:.2f}')
elif operacao == '-':
  sub = primeiro_numero - segundo_numero
  print(f'{sub:.2f}')
elif operacao == '*':
  multiplicacao = primeiro_numero * segundo_numero
  print(f'{multiplicacao:.2f}')
elif operacao == '/':
  divisao = primeiro_numero / segundo_numero
  print(f'{divisao:.2f}')