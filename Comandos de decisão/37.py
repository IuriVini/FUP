def simplificada(x1, x2):
  divisao = x1 % x2
  numerador = x1
  denominador = x2
  while divisao != 0:
    x1 = x2 
    x2 = divisao 
    divisao = x1 % x2
  mdc = x2
    
  numerador = numerador // mdc
  denominador = denominador // mdc
  return numerador, denominador
  
  