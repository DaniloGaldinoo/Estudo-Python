# Exercício 36 - Verificar Formação de Triângulo
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que verifica se três segmentos
# de reta podem formar um triângulo com base
# na regra da desigualdade triangular.

print('|*****************************|')
print('|  *  FORMAÇÃO TRIANGULAR  *  |')
print('|*****************************|')
a = float(input('Insira o valor da primeira reta: '))
b = float(input('Insira o valor da segunda reta: '))
c = float(input('Insira o valor da terceira reta: '))

if a < b+c and b < a+c and c < a+b:
    print('Esses valores FORMAM UM TRIANGULO!')
else:
    print('NÃO FORMAM UM TRIANGULO')