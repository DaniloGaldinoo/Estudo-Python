# Exercício 18 - Cálculo da hipotenusa
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o comprimento da hipotenusa de um triângulo retângulo.

import math

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f"O comprimento da hipotenusa é {hipotenusa:.2f}")