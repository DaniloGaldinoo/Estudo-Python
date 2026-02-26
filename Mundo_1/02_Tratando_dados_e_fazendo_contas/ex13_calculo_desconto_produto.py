# Exercício 13 - Cálculo de desconto em produto
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que calcula o novo preço de um produto com 5% de desconto.

print('Desconto de 5%')
vlr = float(input('Insira o valor do produto: '))
desc = vlr*0.05
vlr = vlr-desc
print('O Novo preço do produto com o desconto de 5% é de R$: {:.2f}'.format(vlr))