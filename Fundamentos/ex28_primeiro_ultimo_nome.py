# Exercício 28 - Primeiro e Último Nome
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que recebe um nome completo
# e exibe o primeiro e o último nome digitado.

nome = str(input('Insira seu nome completo: ')).strip()
print(f'Primeiro: {nome.split()[0]}')
print(f'Ultimo: {nome.split()[-1]}')
