#Faça um programa em que troque todas as ocorrências de uma letra L1 pela letra L2 em uma string. A string e as letras L1 e L2 devem ser fornecidas pelo usuário.
palavra = str(input())
l1= str(input())
l2 = str(input())
p = palavra.replace(l1, l2)
print(p)