# Exercício 19 - Cálculo de seno, cosseno e tangente
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula seno, cosseno e tangente de um ângulo em graus.

import math

# Lê o ângulo em graus
angulo = float(input("Digite o ângulo em graus: "))

# Converte para radianos
radianos = math.radians(angulo)

# Calcula seno, cosseno e tangente
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Mostra os resultados
print(f"O ângulo de {angulo}° tem:")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
