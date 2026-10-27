def fat(x):
  if x == 0 or x == 1:
    return 1
  else:
    return x * fat(x-1)
def sf(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fat(x) * sf(x - 1)

print(sf(4))
