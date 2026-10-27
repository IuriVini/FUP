for i in range(1000, 10000):
  primeiro = i // 100
  segundo = i % 100
  soma = primeiro + segundo 
  quadrado = soma * soma
  if quadrado == i:
    print(i)