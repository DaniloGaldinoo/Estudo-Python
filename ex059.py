from time import sleep
import os
select = 0

print ('*'*20)
print ('{:^20}'.format('CALCULADORA'))
print ('*'*20)

while select != 5:
    num = 1
    n1 = float(input(f'Insira o {num}º numero:  '))
    num += 1
    n2 = float(input(f'Insira o {num}º numero: '))

    while True:
        print('Oque você deseja fazer com os numeros inseridos?')
        print('[1] SOMAR')
        print('[2] MULTIPLICAR')
        print('[3] MAIOR')
        print('[4] NOVOS NUMEROS')
        print('[5] SAIR DO PROGRAMA')
        select = int(input('Escolha: '))
        if select < 1 or select > 5:
            print ('\033[31m' + 'ESCOLHA INVALIDA!'  + '\033[m')
            print ('\033[31m' + 'R E I N I C I A N D O . . .'  + '\033[m')
            sleep(0.5)
            continue
        elif select == 1:
            soma = n1 + n2
            print ('\033[34m' + f'Você escolheu somar!\nA soma de {n1} e {n2} é: {soma}!'  + '\033[m')
            print('-='*20)
        elif select == 2:
            mult = n1 * n2
            print ('\033[34m' + f'Você escolheu multiplicar!\nA multiplicação de {n1} e {n2} é: {mult}'  + '\033[m')
            print('-=' * 20)
        elif select == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print ('\033[34m' + f'Você selecionou Maior!\n O maior numero entre {n1} e {n2} é: {maior}'  + '\033[m')
            print('-=' * 20)
        elif select == 4:
            print (f'\033[34m' + 'Você deseja selecionar outros numeros?'  + '\033[m')
            print('REINICIANDO. . .')
            sleep(0.4)
            break
        elif select == 5:
            print ('\033[31m' + 'S A I N D O . . .\nPROGRAMA FINALIZADO!'  + '\033[m')
            sleep(1.0)
            exit()
