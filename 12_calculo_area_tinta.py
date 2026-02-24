# Exercício 12 - Cálculo de área e quantidade de tinta
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula a área de uma parede e a quantidade de tinta necessária para pintá-la.
# Considerando que 1 litro de tinta cobre 2 m².

print('Calculadora de quantidade de tinta necessária')

altura = float(input('Insira a altura da parede (m): '))
largura = float(input('Insira a largura da parede (m): '))

area = altura * largura
litros_tinta = area / 2

print(f'A área da parede é {area:.2f} m²')
print(f'Serão necessários {litros_tinta:.2f} litros de tinta')