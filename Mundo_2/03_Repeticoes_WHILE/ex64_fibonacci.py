# Exercício 64 - Sequência de Fibonacci
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Gera a sequência de Fibonacci até
# a quantidade de termos desejada pelo usuário.

print ('*'*26)
print ('{:^20}'.format('  SEQUENCIA DE FIBONACCI'))
print ('*'*26)

cont = 0
a = 0
b = 1

n = int(input('Deseja ver a squencia até que numero? Insira -> '))



while cont < n:
    print (a, end=' -> ')
    c = a + b
    a = b
    b = c
    cont += 1

print('FIM')