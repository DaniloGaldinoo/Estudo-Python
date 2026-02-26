# Exercício 67 - Conta e Soma com Break
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário inserir números continuamente
# e calcula a soma total até que seja digitado 999 para encerrar,
# usando break para interromper o loop.

c = s = n = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print (f'A soma dos {c} valores foi de {s}!')