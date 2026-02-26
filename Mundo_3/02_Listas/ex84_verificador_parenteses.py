# Exercício 83 - Verificador de parenteses
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Verificador de parenteses abertos e fechados.

aberto = 0
fechado = 0

exp = str(input('Insira a expressão: '))

for letra in exp:
    if fechado > aberto:
        break
    if letra == '(':
        aberto += 1
    if letra == ')':
        fechado += 1

if aberto == fechado:
    print ('Sua expressão esta Válida!')
else:
    print ('Sua expressão esta Inválida!')