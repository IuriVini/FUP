#Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.
ns = int(input())

h = ns // 3600
ns -= h * 3600

m = ns // 60
ns -= m * 60
s = ns

print(f'{h}')
print(f'{m}')
print(f'{s}')
