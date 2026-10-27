def funcao(x1, x2):
  if x2 % x1 == 0 or x1 % x2 == 0:
    if x1 > x2:
      return x1
    else:
      return x2
  else:
    if x1 % 2 == 0 and x2 % 2 == 0:
      mmc = (x1 / 2) * x2
      return mmc
    else:
      mmc = x1 * x2
      return mmc