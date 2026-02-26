# Exercício 33 - Ano Bissexto
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica se um ano é bissexto
# com base nas regras do calendário gregoriano.

print('------------------------')
print('|* ANO BISSEXTO OU NÃO *|')
print('------------------------')

ano = int(input('Digite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'{ano} é BISSEXTO!')
else:
    print(f'{ano} NÃO é bissexto.')