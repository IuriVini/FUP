#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321. Não utilize strings.
n = input()
ni = int(str(n)[::-1])
print(ni)
