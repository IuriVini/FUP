#Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.
s = 0
for c in range(1, 11):
    c = float(input())
    s += c
print(f'{s:.2f}')