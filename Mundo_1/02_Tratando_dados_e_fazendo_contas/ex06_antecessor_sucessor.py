# Exercício 06 - Antecessor e Sucessor
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que mostra o antecessor e o sucessor de um número digitado.

print('=' * 30)
print('|  SUCESSOR E ANTECESSOR  |')
print('=' * 30)

numero = int(input('Digite o número: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor de {numero} é {antecessor} e o sucessor é {sucessor}.')