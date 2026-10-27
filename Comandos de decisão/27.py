repeticao = int(input())
numero = float(input())
maior = numero
menor = numero
for c in range(repeticao -1):
  numero = float(input())
  if numero > maior:
    maior = numero
  if numero < menor:
    menor = numero
print(f'{menor:.2f}')
print(f'{maior:.2f}')
