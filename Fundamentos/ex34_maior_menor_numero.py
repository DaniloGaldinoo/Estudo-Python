# Exercício 34 - Maior e Menor Número
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que recebe três números
# e identifica qual é o maior e o menor valor digitado.

print('---------------------------')
print('| IDENTIFICADOR DE NUMEROS |')
print('---------------------------')

n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
n3 = int(input('Insira o 3º número: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')