def funcao(x):
  if x < 0:
    return False
  i = 0
  while i * i < x:
    i = i + 1
  if i * i == x:
    return True
  else:
    return False