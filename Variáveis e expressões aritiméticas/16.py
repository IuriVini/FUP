#Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0, 0).
x = float(input())
y = float(input())
c = (x ** 2 + y ** 2)**0.5
print(f'{c:.2f}')