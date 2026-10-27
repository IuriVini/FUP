valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())
v1 = 0
v2 = 0 
v3 = 0
if valor_1 > valor_2:
  if valor_1 > valor_3:
    v3 = valor_1
    if valor_2 > valor_3:
      v2 = valor_2
      v1 = valor_3
    else:
      v2 = valor_3
      v1 = valor_2
  else:
    v1 = valor_2
    v2 = valor_1
    v3 = valor_3
elif valor_1 < valor_2:
  if valor_1 < valor_3:
    v1 = valor_1
    if valor_2 > valor_3:
      v2 = valor_3
      v3 = valor_2
    else:
      v2 = valor_2
      v3 = valor_3
  else:
    v3 = valor_2
    v2 = valor_1
    v1= valor_3
elif valor_1 == valor_2:
  if valor_1 == valor_3:
    v1 = valor_1
    v2 = valor_1
    v3 = valor_1
  else:
    if valor_1 > valor_3:
      v1 = valor_3
      v2 = valor_1
      v3 = valor_1
    else:
      v1 = valor_1
      v2 = valor_1
      v3 = valor_3
else:
  if valor_1 == valor_3:
    if valor_1 > valor_2:
      v1 = valor_2
      v2 = valor_1
      v3 = valor_1
    else:
      v1 = valor_1
      v2 = valor_1
      v3 = valor_1
  else:
    if valor_2 > valor_1:
      v1 = valor_1
      v2 = valor_2
      v3 = valor_2
    else:
      v1 = valor_2
      v2 = valor_2
      v3 = valor_1
print(v1)
print(v2)
print(v3)