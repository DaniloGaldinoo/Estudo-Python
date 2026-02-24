# Exercício 46 - Jogo Jokenpô
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Jogo de Pedra, Papel e Tesoura contra
# o computador utilizando laço de repetição,
# módulo random e time.

import random
import time
while True:

    print ('\033[32m' + '*' * 13 + '\033[m')
    print ('\033[34m' + '* JO KEN PO *' + '\033[m')
    print ('\033[32m' + '*' * 13 + '\033[m')

    print ('ESCOLHA SUA ARMA!')
    print ('[1] - PEDRA')
    print ('[2] - PAPEL')
    print ('[3] - TESOURA')
    esc = int(input('QUAL VOCE ESCOLHE : '))
    if esc < 1 or esc > 3:
        print('ENTRADA INVALIDA!')
        continue

    print ('-' *21)
    print ('P E N S A N D O . . .')
    print ('-' *21)
    time.sleep(0.8)
    pc = random.randint(1, 3)

    if pc == 1 and esc == 1:
        print('EMPATE!!!')
        print('O COMPUTADOR TAMBÉM ESCOLHEU PEDRA!')
    elif pc == 1 and esc == 2:
        print('VOCÊ VENCEU!!')
        print('O COMPUTADOR ESCOLHEU PEDRA!')
    elif pc == 1 and esc == 3:
        print('VOCÊ PERDEU!!!')
        print('O COMPUTADOR ESCOLHEU PEDRA!')
    elif pc == 2 and esc == 1:
        print('VOCÊ PERDEU!!!')
        print('O COMPUTADOR ESCOLHEU PAPEL!')
    elif pc == 2 and esc == 2:
        print('EMPATE!!!')
        print('O COMPUTADOR TAMBÉM ESCOLHEU PAPEL!')
    elif pc == 2 and esc == 3:
        print('VOCÊ GANHOU!!!')
        print('O COMPUTADOR ESCOLHEU PAPEL!')
    elif pc == 3 and esc == 1:
        print('VOCÊ GANHOU!!!')
        print('O COMPUTADOR ESCOLHEU TESOURA!')
    elif pc == 3 and esc == 2:
        print('VOCÊ PERDEU!!!')
        print('O COMPUTADOR ESCOLHEU TESOURA!')
    elif pc == 3 and esc == 3:
        print('EMPATE!!!')
        print('O COMPUTADOR TAMBÉM ESCOLHEU TESOURA!')
    else:
        print('ESCOLHA INVALIDA!')

    print ('-' *30)
    n = input('Você deseja SAIR do jogo? Se SIM, digite [1]: ').strip()
    if n == 1:
        break
