# Exercício 04 - Soma de dois números
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que solicita dois números ao usuário e exibe a soma entre eles.

print('*********************************')
print('|   Vamos somar dois números?   |')
print('*********************************')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

soma = n1 + n2

print('A soma entre {} e {} é {}'.format(n1, n2, soma))