palavra = str(input())
caractere = str(input())
vogais = "aeiouAEIOU"
vogal = 0
for letra in palavra:
  if letra in vogais:
    vogal += 1
print(vogal)
palavra_trocada = "".join(caractere if letra in vogais else letra for letra in palavra)
print(palavra_trocada)
