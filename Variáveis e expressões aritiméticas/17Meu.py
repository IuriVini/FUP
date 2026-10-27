amigo_1 = float(input())
amigo_2 = float(input())
amigo_3 = float(input())
premio_total = float(input())

valor_total = amigo_1 + amigo_2 + amigo_3
porcentagem_amigo1 = amigo_1 / valor_total
porcentagem_amigo2 = amigo_2 / valor_total
porcentagem_amigo3 = amigo_3 / valor_total

premio_amigo1 = porcentagem_amigo1 * premio_total
premio_amigo2 = porcentagem_amigo2 * premio_total
premio_amigo3 = porcentagem_amigo3 * premio_total

print(f'{premio_amigo1:.2f}')
print(f'{premio_amigo2:.2f}')
print(f'{premio_amigo3:.2f}')
print(f'{premio_total:.0f}')
