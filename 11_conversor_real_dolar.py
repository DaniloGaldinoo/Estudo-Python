# Exercício 11 - Conversor de Real para Dólar
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que converte um valor em reais para dólares usando uma taxa fixa.

print("Conversor Real/Dollar")
r = float(input('Insira o valor em R$: '))
d = r/3.27
print('Voce pode comprar {:.2f} Dolares com essa quantia!'.format(d))