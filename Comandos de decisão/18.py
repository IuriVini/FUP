def funcao(x):
  if x[0] == '0':
    dia = x[1]
  else:
    dia = x[0:2]
  if x[3:5] == "01":
    mes_extenso = "janeiro"
  elif x[3:5] == "02":
    mes_extenso = "fevereiro"
  elif x[3:5] == "03":
    mes_extenso = "marco"
  elif x[3:5] == "04":
    mes_extenso = "abril"
  elif x[3:5] == "05":
    mes_extenso = "maio"
  elif x[3:5] == "06":
    mes_extenso = "junho"
  elif x[3:5] == "07":
    mes_extenso = "julho"
  elif x[3:5] == "08":
    mes_extenso = "agosto"
  elif x[3:5] == "09":
    mes_extenso = "setembro"
  elif x[3:5] == "10":
    mes_extenso = "outubro"
  elif x[3:5] == "11":
    mes_extenso = "novembro"
  elif x[3:5] == "12":
    mes_extenso = "dezembro"
  ano = x[6:10]
  return f"{dia} de {mes_extenso} de {ano}" 
    
      
