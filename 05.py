#Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .
import math 
r = float(input())
v = r**3 * math.pi * 4 / 3
a = 4 * math.pi * r**2
print(f'{v:.2f}')
print(f'{a:.2f}')
