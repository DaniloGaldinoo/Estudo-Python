# Exercício 31 - Par ou Ímpar
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica se um número
# digitado é par ou ímpar utilizando o operador módulo.

print('----------------')
print('| PAR OU IMPAR |')
print('----------------')

n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'{n} é PAR!')
else:
    print(f'{n} é ÍMPAR!')