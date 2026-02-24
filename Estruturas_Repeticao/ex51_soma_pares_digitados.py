# Exercício 51 - Soma dos Números Pares
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Lê 6 números inteiros e soma
# apenas os valores pares digitados.

soma = 0
num = 1
for c in range (1, 7):

    n = int(input(f'Insira o {num}º numero: '))
    num += 1
    if n % 2 == 0:
        soma += n
print(f'A soma total é: {soma}')