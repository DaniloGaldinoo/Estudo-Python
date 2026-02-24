# Exercício 17 - Parte inteira de um número
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que mostra a parte inteira de um número real usando o módulo math.

from math import trunc

numero = float(input('Digite um número: '))

parte_inteira = trunc(numero)

print(f'O número {numero} tem a parte inteira {parte_inteira}')