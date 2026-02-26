# Exercício 75 - Sorteio de Números
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Sorteia 5 números aleatórios entre 1 e 10,
# armazena em uma tupla e mostra o maior e menor valor sorteado.

from random import randint
aleat = tuple((randint(1,10) for c in range(1, 6)))

print (f'Os valores sorteados foram: {aleat}')
print (f'O maior valor sorteado foi: {max(aleat)}')
print (f'O menor valor sorteado foi: {min(aleat)}')
