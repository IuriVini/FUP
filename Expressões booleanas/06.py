idade = int(input())
tempo_de_servico = int(input())
if idade >= 65 or tempo_de_servico >= 30 or idade >= 60 and tempo_de_servico >= 25:
  print("Pode se aposentar")
else:
  print("Nao pode se aposentar")