def funcao(x1,x2):
  fat_x1 = 1
  fat_x2 = 1
  fat_parentese = 1
  subtracao = x1 - x2
  for n in range(1, x1+1):
    fat_x1 *= n
  for k in range(1, x2+1):
    fat_x2 *= k
  for c in range (1, subtracao +1):
    fat_parentese *= c
  formula = fat_x1 / (fat_x2*fat_parentese)  
  return formula