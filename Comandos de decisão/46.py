palavra = input().lower()
palavra = palavra.replace(" ", "")
palavra = palavra.replace("-", "")
palavra = palavra.replace(",", "")
palavra = palavra.replace(".", "")
contrario = palavra[::-1]
if palavra == contrario:
  print(True)
else:
  print(False)