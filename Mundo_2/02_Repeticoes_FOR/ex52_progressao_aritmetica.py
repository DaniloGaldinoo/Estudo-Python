# Exercício 52 - Progressão Aritmética
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Mostra os 10 primeiros termos
# de uma Progressão Aritmética.

print('|{}|'.format('*'*31))
print('|     PROGRESSAO ARITMETICA     |')
print('|{}|'.format('*'*31))

n = int(input('Isira o primeiro termo: '))
r = int(input('Isira a razão: '))

for cont in range (1, 11):
    print(n)
    n += r