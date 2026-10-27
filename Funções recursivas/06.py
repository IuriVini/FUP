def funcao(x):
  if x == 0:
    print("0")
  else:
    print(x)
    funcao(x - 1)
x = int(input())
funcao(x)