#Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.
s = 0
n = int(input())
for c in range(0, n+1):
    s += c
print(s)