# Exercício 69 - Par ou Ímpar
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Permite ao usuário jogar Par ou Ímpar
# contra o computador, contando quantas vezes o
# jogador venceu até perder.

from random import randint
print ('*'*22)
print ('{:^22}'.format('*    PAR OU IMPAR    *'))
print ('*'*22)

print ('VAMOS JOGAR?')
print('='*22)
perder = 0
ven = 0

while perder == 0:
    n = int(input('Diga um valor: '))
    pi = str(input('Par ou Impar? [P/I] : '))
    print('-'*22)
    ncomp = randint (1,10)
    soma = ncomp + n

    if soma % 2 == 0 and pi == 'P':
        print(f'Você jogou {n} e o computador jogou {ncomp}. Total de {soma}! DEU PAR.')
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-=' * 10)
        ven += 1
    elif soma % 2 == 1 and pi == 'I':
        print(f'Você jogou {n} e o computador jogou {ncomp}. Total de {soma}! DEU IMPAR')
        print('Você VENCEU!\nVamos jogar novamente...')
        print('-=' * 10)
        ven += 1
    else:
        print('Você PERDEU! hahaha')
        print(f'Você jogou {n} e o computador jogou {ncomp}. Total de {soma}!')
        print(f'GAME OVER, Você venceu {ven} vezes.')
        break
