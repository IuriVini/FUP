#Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
valor = int(input())

Nota_100 = valor // 100
valor = valor % 100

Nota_50 = valor // 50
valor = valor % 50

Nota_20 = valor // 20
valor = valor % 20

Nota_10 = valor // 10
valor = valor % 10

Nota_5 = valor // 5
valor = valor % 5

Nota_2 = valor // 2
valor = valor % 2

Nota_1 = valor // 1
valor = valor % 1

print(Nota_100)
print(Nota_50)
print(Nota_20)
print(Nota_10)
print(Nota_5)
print(Nota_2)
print(Nota_1)