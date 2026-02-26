# Exercício 29 - Jogo de Adivinhação
# Curso: Python
# Autor: Danilo Galdino
# Descrição: Programa que sorteia um número entre 0 e 5
# e solicita que o usuário tente adivinhar o valor,
# exibindo o resultado após uma breve pausa.

import random
from time import sleep

nome = str(input ('Ola, Qual seu nome? '))
num = int(input (f'Ola {nome}, tudo bem? Tente adivinhar o numero inteiro entre 0 e 5 que eu sorteei!  '))

if num > 5:
    print('Numero Invalido, Maior que 5! REINICIE!!')

else:
    sorteado = random.randint(0, 5)
    print ('P E N S A N D O . . .')
    sleep(3)
    print (f'O numero sorteado foi: {sorteado}\nVocê escolheu o n umero: {num}.')

    if sorteado == num:
        print('-------------------')
        print('| P A R A B E N S |')
        print('-------------------')
        print('Você acertou o numero sorteado!')
    else:
        print('-------------------')
        print('|  Que Penaaa!!   |')
        print('-------------------')
        print('Você errou o numero sorteado!')
