soma = 0
repetição = 0
while repetição < 10:
  numero = float(input())
  if numero > 0:
    soma = soma + numero
    repetição = repetição + 1
  else:
    repetição = repetição
media = soma / 10
print(f'{media:.2f}')  