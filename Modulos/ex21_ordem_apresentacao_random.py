# ==========================================================
# Exercício 21 - Ordem Random
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que Sorteia uma ordem para apresentação dos alunos.
# ==========================================================

import random
print ('*'*58)
print ('| SORTEIO PARA SABER A ORDEM DE APRESENTAÇÃO DOS ALUNOS! |')
print ('*'*58)
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))

lista = [a1, a2, a3, a4]
random.shuffle(lista)

print (f'A ordem a ser apresentada é: {lista}')