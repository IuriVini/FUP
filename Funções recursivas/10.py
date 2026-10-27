def funcao(x):
  if x == 1:
    return 1
  elif x == 2:
    return 2
  else:
    seq1 = 2 * funcao(x - 1)
    seq2 = 3 * funcao(x - 2)
    return seq1 + seq2
