import random
from time import sleep
acertou = 0
palpite = 0
nome = str(input ('Ola, Qual seu nome? '))
sorteado = random.randint(0, 10)

while acertou == 0:
    num = int(input(f'Ola {nome}, tudo bem? Tente adivinhar o numero inteiro entre 0 e 10 que eu sorteei!  '))

    if num < 0 or num > 10:
        print('Numero Invalido, Maior que 10! REINICIE!!')
        continue

    else:
        print ('P E N S A N D O . . .')
        sleep(0.4)
        palpite += 1

        if sorteado == num:
            acertou = 1
            print('-------------------')
            print('| P A R A B E N S |')
            print('-------------------')
            print('Você acertou o numero sorteado!')
            if palpite == 1:
                print('UAU!!! ACERTOU DE PRIMEIRA!')
            else:
                print (f'PARABÉNS! FORAM NECESSARIOS {palpite} PALPITES!')
        else:
            print('-------------------')
            print('|  Que Penaaa!!   |')
            print('-------------------')
            print('Você errou o numero sorteado!\nTENTE NOVAMENTE!')
