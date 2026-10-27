#Leia uma string contendo letras de uma frase, inclusive os espaços em branco. Retirar os espaços em branco e depois escrever a frase resultante.
palavra = str(input())
palavra_junta = palavra.replace(" ", "")
print(palavra_junta)