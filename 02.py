#Faça um programa que, a partir das medidas dos lados de um retângulo, lidos via teclado, calcule a área e o perímetro deste retângulo.
b = float(input())
h = float(input())
a = b * h
p = 2 * (b + h)
print(f'{a:.2f}')
print(f'{p:.2f}')
