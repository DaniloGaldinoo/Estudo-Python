# Exercício 50 - Tabuada com Laço For
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Mostra a tabuada de um número
# informado pelo usuário utilizando laço for.


n1 = int(input('Insira o numero que quer ver a tabuada: '))
print('|{}|'.format('*'*23))
print('|     T A B U A D A     |')
print('|{}|'.format('*'*23))

for c in range (1, 11):
    print(f'|    {c:2} x {n1:2} = {c*n1:2}       |')

print('|{}|'.format('*'*23))