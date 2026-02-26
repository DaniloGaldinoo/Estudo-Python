# Exercício 15 - Conversor de Celsius para Fahrenheit
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que converte temperatura de Celsius para Fahrenheit.

c = float(input('Digite a temperatura em ºC, para converte-la em ºF : '))
f = (c * 9/5) + 32

print('{}ºC convertido ficam {}ºF'.format(c,f))