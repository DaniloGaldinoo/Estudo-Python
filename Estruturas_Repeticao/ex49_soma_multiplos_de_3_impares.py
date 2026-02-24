# Exercício 49 - Soma de Múltiplos de 3 Ímpares
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Soma todos os números ímpares
# múltiplos de 3 no intervalo de 1 a 500.

s = 0
for c in range (1, 501):
    if c % 3 == 0 and c % 2 == 1:
        s += c
        print (c)
print (f'A soma é {s}')
