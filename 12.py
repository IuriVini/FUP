'''Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
◦ O primeiro ganhador receberá 46%;
◦ O segundo ganhador receberá 32%;
◦ O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.'''

t = float(input())
g1 = t * 0.46
g2 = t * 0.32
g3 = t * 0.22
print(f'{g1:.2f}')
print(f'{g2:.2f}')
print(f'{g3:.2f}')
