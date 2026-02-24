# Exercício 76 - Análise de Tupla
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário digitar 4 números,
# armazenados em uma tupla, e exibe quantas vezes
# o número 9 apareceu, a posição do número 3 (se existir)
# e todos os números pares digitados.

t = ()
tp = ()
for c in range(1,5):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        tp = tp + (n,)
    t = t + (n,)

print(f'Os numeros digitados foram: {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na posição {t.index(3)+1}')
else:
    print('O valor 3 não apareceu em nenhuma posição.')
print(f'Os numeros pares digitados foram: {tp}')