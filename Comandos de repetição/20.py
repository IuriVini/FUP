def funcao(x):
  for b in range(1, x+1):
    print('*' * b)
  a = x - 1
  for i in range(x - 1):
    print('*' * a)
    a = a -1
funcao(4)
print(funcao)  