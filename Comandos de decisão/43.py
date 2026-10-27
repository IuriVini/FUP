nome = input()
idade = int(input())
if idade > 0:
  
  menor_idade = idade
  maior_idade = idade
  nome_jovem = nome
  nome_velho = nome
  
  while idade >=0:
    nome = input()
    idade = int(input())
    if idade > 0:
      if idade < menor_idade:
        menor_idade = idade
        nome_jovem = nome
      if idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    else:
      break
      
    
print(nome_jovem)
print(menor_idade)
print(nome_velho)
print(maior_idade)