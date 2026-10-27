palavra = str(input())
frase_final = ''
for letra in palavra:
   codigo = ord(letra) +1
   letra_nova = chr(codigo)
   frase_final = frase_final + letra_nova
print(frase_final)