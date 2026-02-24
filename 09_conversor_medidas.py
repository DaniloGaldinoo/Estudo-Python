# Exercício 09 - Conversor de medidas
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que converte metros em centímetros e milímetros.

print('=' * 26)
print('| CONVERSOR DE MEDIDAS |')
print('=' * 26)

metros = float(input('Insira o valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'{metros} metros em centímetros é: {centimetros} cm')
print(f'{metros} metros em milímetros é: {milimetros} mm')