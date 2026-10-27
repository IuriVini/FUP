numero = int(input())
if numero % 3 == 0 and numero % 5 != 0 or numero % 5 == 0 and numero % 3 != 0:
  print(True)
else:
  print(False)