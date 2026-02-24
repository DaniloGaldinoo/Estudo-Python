# Exercício 68 - Tabuada
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário gerar a tabuada de
# um número inteiro, repetindo o processo até que
# seja digitado um valor negativo.

print('*'*22)
print('{:^22}'.format('*   TABUADA   *'))
print('*'*22)

n = c = 0
multiplicador = 1

while n >= 0:
    n = int(input('Quer ver a tabuada de qual valor?  -> '))
    print('-=' * 10)
    if n < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre')
        break
    while c < 10:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1
        c += 1
    print('-=' * 10)
    c = 0
    multiplicador = 1

print ('*'*22)
print ('{:^22}'.format('*   TABUADA   *'))
print ('*'*22)
n = c = 0
multiplicador = 1

while n >=0:
    n = int(input('Quer ver a tabuada de qual valor?  -> '))
    print('-=' * 10)
    if n < 0:
        print ('PROGRAMA TABUADA ENCERRADO. Volte sempre')
        break
    while c < 10:
        print(f'{n} x {multiplicador} = {n * multiplicador}')
        multiplicador += 1
        c += 1
    print('-=' * 10)
    c = 0
    multiplicador = 1