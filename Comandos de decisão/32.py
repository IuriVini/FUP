numero_1 = int(input())
numero_2 = int(input())
if numero_1 > numero_2:
  dividendo = numero_1
  divisor = numero_2
else:
  dividendo = numero_2
  divisor = numero_1
acumulado = divisor
quociente = 0
while acumulado <= dividendo:
  quociente +=1
  acumulado +=divisor
print(quociente)