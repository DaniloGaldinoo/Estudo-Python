# Exercício 10 - Tabuada de um número
# Curso de Python
# Autor: Danilo Galdino
# Descrição: Programa que mostra a tabuada de um número de 1 a 10.

n1 = int(input('Insira o numero que quer ver a tabuada: '))
n2 = 1
print('|{}|'.format('*'*23))
print('|     T A B U A D A     |')
print('|{}|'.format('*'*23))

print('|      {} x {:2} = {:2}      |'.format(n1, n2, n1*1))
print('|      {} x {:2} = {:2}      |'.format(n1, n2, n1*2))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+2, n1*3))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+3, n1*4))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+4, n1*5))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+5, n1*6))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+6, n1*7))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+7, n1*8))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+8, n1*9))
print('|      {} x {:2} = {:2}      |'.format(n1, n2+9, n1*10))
print('|{}|'.format('*'*23))

#Usei o metodo .format para relembrar e fixar conhecimento