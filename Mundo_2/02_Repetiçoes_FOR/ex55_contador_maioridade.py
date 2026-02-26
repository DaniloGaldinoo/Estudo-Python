# Exercício 55 - Contador de Maioridade
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Lê o ano de nascimento de 7 pessoas
# e informa quantas são maiores e menores de idade.

maior = 0
menor = 0

for c in range (1, 8):
    ano = int(input(f'Insira o ano de nascimento da {c}º pessoa: '))
    tot = 2025-ano
    if tot > 18:
        maior += 1
    else:
        menor += 1

print(f'No total temos {maior} maiores de idade e {menor} menores de idade!')