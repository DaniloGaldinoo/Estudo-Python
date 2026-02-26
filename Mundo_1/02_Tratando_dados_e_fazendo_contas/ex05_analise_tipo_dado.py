# Exercício 05 - Análise de tipo de dado
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que analisa as características de um valor digitado pelo usuário.

valor = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúsculas?', valor.isupper())
print('Está em minúsculas?', valor.islower())
print('Está capitalizada?', valor.istitle())