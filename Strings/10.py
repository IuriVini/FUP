#Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no final da primeira, retornando o resultado da verificação.
s1 = str(input())
s2 =str(input())
saida = s1.endswith(s2)
print(saida)