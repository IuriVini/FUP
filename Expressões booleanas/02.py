texto = str(input())
vogais = "aeiouAEIOU"
texto_sem_vogal = "".join([char for char in texto if char not in vogais])
print(texto_sem_vogal)