n = int(input())
for l in range(0, n):
  a = ''
  for k in range(0,l+1):
    sub = l - k
    fat1 = 1
    for f in range(1, l+1):
      fat1 *= f
    fat2 = 1
    for c in range(1, k+1):
      fat2 *= c
    fat_parentese = 1      
    for b in range(1, sub+1):
      fat_parentese *= b
    r= fat1 // (fat2*fat_parentese)
    a = a + str(r) + ' '
  print(a)    