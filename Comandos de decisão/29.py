numero = int(input())
if numero != 1:
  primo = 0
  for i in range(1, numero +1):
    if numero % i == 0:
      primo += 1
  if primo > 2:
    print('Nao primo')
  else:
    print('Primo')
else:
  print('Nao primo')