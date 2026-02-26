# Exercício 47 - Contagem Regressiva
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que realiza uma contagem
# regressiva de 10 até 0 utilizando laço for
# e módulo time.

import time

print ('\033[32m' + '*' * 23 + '\033[m')
print ('\033[34m' + '* INICIANDO CONTAGEM! *' + '\033[m')
print ('\033[32m' + '*' * 23 + '\033[m')

for c in range (10, -1, -1):
    print (c)
    time.sleep (1.0)

print ('\033[32m' + '*' * 21 + '\033[m')
print ('\033[34m' + '* FELIZ ANO NOVO!!! *' + '\033[m')
print ('\033[32m' + '*' * 21 + '\033[m')