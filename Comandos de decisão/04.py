valor_1 = float(input())
valor_2 = float(input())
valor_3 = float(input())
maior = 0
if valor_1 < valor_2:
  valor_1 = valor_2
if valor_1 < valor_3:
  valor_1 = valor_3
print(f"{valor_1:.2f}")