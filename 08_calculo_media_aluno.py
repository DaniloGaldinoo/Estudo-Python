# Exercício 08 - Cálculo de média do aluno
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula a média de duas notas de um aluno.

print('=' * 20)
print('| ESCOLA GALDINO |')
print('=' * 20)

print('Vamos calcular a média do aluno!')

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do aluno é {media:.1f}')