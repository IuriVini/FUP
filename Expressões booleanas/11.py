def funcao(x):
  if "/" == x[2] and "/" == x[5]:
    dia = x[0:2]
    if dia.isdigit():
      dia_int = int(dia)
    else:
      return 0, 0, 0
    mes = x[3:5]
    if mes.isdigit():
      mes_int = int(mes)
    else:
      return 0, 0, 0
    ano = x[6:11]
    if ano.isdigit() and len(ano) == 4 :
      ano_int = int(ano)
    else:
      return 0, 0, 0
    return dia_int, mes_int, ano_int
  else:
    return 0, 0, 0