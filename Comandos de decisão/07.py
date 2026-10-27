salario = float(input())
valor_prestacao = float(input())
porcentagem = salario * 0.2
if valor_prestacao > porcentagem:
  print('Emprestimo nao concedido')
else:
  print("Emprestimo concedido")