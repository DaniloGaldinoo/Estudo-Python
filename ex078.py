valores = []

for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

print(f'Voce digitou os valores: {valores}')

maior = max(valores)
menor = min(valores)

pos_maior = []
pos_menor = []

for pos, valor in enumerate(valores):
    if valor == maior:
        pos_maior.append(int(pos))
for pos, valor in enumerate(valores):
    if valor == menor:
        pos_menor.append(int(pos))

print(f'O maior valor digitado foi {max(valores)} nas posições {pos_maior}')
print(f'O menor valor digitado foi {min(valores)} nas posições {pos_menor}')
